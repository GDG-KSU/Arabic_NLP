import re
import pyarabic.araby as araby

def clean_arabic_text(text):
    text = araby.strip_tashkeel(text)
    text = re.sub(r"[إأآ]", "ا", text)
    text = re.sub(r"ة", "ه", text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    tokens = araby.tokenize(text)
    return tokens

try:
    with open("NLP.txt", "r", encoding="utf-8") as f:
        user_text = f.read()

    result = clean_arabic_text(user_text)

    if result and len(result) >= 50:
        print(f"Success! Processed {len(result)} words.")
        print("Cleaned Tokens:", result)
    else:
        print(f"Warning: Text is too short ({len(result)} words). Minimum 50 required.")
except FileNotFoundError:
    print("Error: Please create a file named 'NLP.txt' first.")