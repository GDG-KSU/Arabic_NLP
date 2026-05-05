import re
import sys

import pyarabic.araby as araby


def clean_arabic_text(text):
    """Clean Arabic text."""
    text = araby.strip_tashkeel(text)
    text = re.sub(r"[إأآ]", "ا", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    tokens = araby.tokenize(text)
    return tokens


def main():
    """Run cleaner."""
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            user_text = file.read()

        result = clean_arabic_text(user_text)

        if result and len(result) >= 50:
            print(f"Success! Processed {len(result)} words.")
            print("Cleaned Tokens:", result)
        else:
            count = len(result) if result else 0
            print(f"Warning: Text too short ({count} words). Min 50 required.")
    except FileNotFoundError:
        print("Error: Please create 'input.txt' first.")


if __name__ == "__main__":
    main()