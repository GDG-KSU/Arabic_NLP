import sys
from pathlib import Path
from pipeline import build_pipeline, process, clean_tokens

def main():
    input_path = Path("data/raw/NLP.txt")
    output_path = Path("data/processed/Cleaned_Dataset.txt")

    if not input_path.exists():
        print(f"Error: Could not find {input_path}")
        sys.exit(1)

    print("Initializing Arabic NLP pipeline...")
    nlp = build_pipeline()

    print(f"Processing data from {input_path}...")
    
    with input_path.open("r", encoding="utf-8") as infile, \
         output_path.open("w", encoding="utf-8") as outfile:
        
        for line in infile:
            line = line.strip()
            if not line:
                continue

            doc = process(line, nlp)
            tokens = clean_tokens(doc)
            
            cleaned_line = " ".join(tokens)
            
            if cleaned_line:
                outfile.write(cleaned_line + "\n")

    print(f"Success. Cleaned dataset saved to {output_path}")

if __name__ == "__main__":
    main()