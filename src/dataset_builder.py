import sys
from pathlib import Path

import pandas as pd
from pipeline import build_pipeline, clean_tokens, process

import sys
import csv

# Dynamically find the maximum CSV field size your specific OS allows
max_int = sys.maxsize
while True:
    try:
        csv.field_size_limit(max_int)
        break
    except OverflowError:
        max_int = int(max_int / 10)

csv.field_size_limit(max_int)

def convert_csv_to_parquet(csv_path: Path) -> Path:
    """Intercepts a CSV, converts it to Parquet, and returns the new file path."""
    print(f"🔄 Intercepted CSV. Converting {csv_path.name} to Parquet format...")
    try:
        # Using the python engine to safely parse normal commas and quotes.
        df = pd.read_csv(
            csv_path,
            encoding="utf-8-sig",
            engine="python",
            on_bad_lines="warn"
        )
        
        # Create a new path with the .parquet extension in the same directory
        parquet_path = csv_path.with_suffix(".parquet")
        
        # Save the raw data as a Parquet file
        df.to_parquet(parquet_path, engine="pyarrow", index=False)
        
        print(f"✅ Converted successfully. New raw file: {parquet_path.name}")
        return parquet_path
        
    except Exception as e:
        print(f"❌ Failed to convert CSV to Parquet: {e}")
        sys.exit(1)


def build_dataset(input_path: Path, output_path: Path):
    if not input_path.exists():
        print(f"Error: Could not find {input_path}")
        sys.exit(1)

    # 1. FILE TYPE ROUTING & CONVERSION
    if input_path.suffix == ".csv":
        # Convert the CSV and update the input path to point to the new Parquet file
        input_path = convert_csv_to_parquet(input_path)
    elif input_path.suffix != ".parquet":
        print(f"Error: Unsupported file type '{input_path.suffix}'.")
        print("Allowed types: .csv, .parquet")
        sys.exit(1)

    # 2. INGESTION (At this point, input_path is guaranteed to be a .parquet file)
    print(f"Loading dataset from {input_path}...")
    try:
        df = pd.read_parquet(input_path, engine="pyarrow")
    except Exception as e:
        print(f"Error reading Parquet file: {e}")
        sys.exit(1)

    if "text" not in df.columns:
        print(f"Error: Could not find a 'text' column. Columns found: {list(df.columns)}")
        sys.exit(1)

    print("Initializing Arabic NLP pipeline...")
    nlp = build_pipeline()

    print("Processing NLP pipeline on the 'text' column... (This may take a minute)")

    def apply_pipeline(raw_text):
        if not isinstance(raw_text, str):
            return ""
        doc = process(raw_text, nlp)
        tokens = clean_tokens(doc)
        return " ".join(tokens)

    # Apply the NLP pipeline exclusively to the text column
    df["text"] = df["text"].apply(apply_pipeline)

    # Drop any rows where the cleaning process left an empty string
    df = df[df["text"].str.strip() != ""]

    # 3. OUTPUT
    df.to_parquet(output_path, engine="pyarrow", index=False)
    print(f"Success. Cleaned dataset saved to {output_path}")


def main():
    """
    DATA ARCHITECTURE NOTE: Why Parquet?
    We strictly export to and prefer .parquet over .csv for three reasons:
    1. Size Limits: GitHub has a 100MB hard limit per file. CSVs bloat quickly; 
       Parquet compresses data natively, often shrinking files by 70-80%.
    2. Speed: Parquet is a columnar format. Pandas/PyArrow reads it exponentially 
       faster than parsing line-by-line CSV text.
    3. Type Safety: CSVs break easily on rogue commas or line breaks in text data. 
       Parquet locks the schema and data types into the file itself.
    
    * Note: If a .csv is provided as the input, this script will automatically 
      convert it to a raw .parquet file before processing to ensure stability.
    """
    # You can now safely leave the default input as the .csv 
    # The script will handle the conversion automatically on the first run.
    default_input = Path("data/raw/final_hybrid_dataset_10k_cleaned.csv")
    default_output = Path("data/processed/Cleaned_Dataset.parquet")
    build_dataset(default_input, default_output)


if __name__ == "__main__":
    main()
