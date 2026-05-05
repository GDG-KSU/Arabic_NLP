import re

import pyarabic.araby as araby


def clean_arabic_text(text):
    """Clean text."""
    text = araby.strip_tashkeel(text)
    text = re.sub(r"[إأآ]", "ا", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    tokens = araby.tokenize(text)
    return tokens


def main():
    """Main function."""
    try:
        with open("NLP.txt", "r", encoding="utf-8") as file:
            user_text = file.read()
        result = clean_arabic_text(user_text)
        if result and len(result) >= 50:
            print(f"Success! Processed {len(result)} words.")
            print(result)
        else:
            count = len(result) if result else 0
            print(f"Warning: Too short ({count} words).")
    except FileNotFoundError:
        print("Error: NLP.txt not found.")


if __name__ == "__main__":
    main()