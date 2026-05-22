import sys
from pathlib import Path
from pipeline import build_pipeline, clean_tokens, process

# We added input_path and output_path as parameters with default values
def build_dataset(input_path: Path, output_path: Path):
    if not input_path.exists():
        print(f"Error: Could not find {input_path}")
        sys.exit(1)

    print("Initializing Arabic NLP pipeline...")
    nlp = build_pipeline()

    print(f"Processing data from {input_path}...")

    with input_path.open("r", encoding="utf-8") as infile, output_path.open(
        "w", encoding="utf-8"
    ) as outfile:
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


def main():
    default_input = Path("data/raw/NLP.txt")
    default_output = Path("data/processed/Cleaned_Dataset.txt")
    build_dataset(default_input, default_output)

if __name__ == "__main__":
    main()
