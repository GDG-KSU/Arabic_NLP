import re

import pyarabic.araby as araby
import requests
from bs4 import BeautifulSoup


def clean_arabic_text(text):
    text = araby.strip_tashkeel(text)

    # Normalizing Letters
    text = re.sub(r"[إأآ]", "ا", text)
    text = re.sub(r"ة", "ه", text)

    # Cleaning links
    text = re.sub(r"http\S+|www\S+", "", text)

    # Cleaning Non Arabic characters
    text = re.sub(r"[^\u0600-\u06FF\s]", " ", text)

    # Space Cleaning
    text = re.sub(r"\s+", " ", text).strip()

    return text


def scrape_arabic_article(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.get_text() for p in paragraphs])
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""


def save_extensive_dataset(url_list, filename="Cleaned_Dataset.txt"):
    with open(filename, mode="w", encoding="utf-8") as file:
        for url in url_list:
            print(f"Scraping: {url}...")
            raw_text = scrape_arabic_article(url)
            if raw_text:
                cleaned_text = clean_arabic_text(raw_text)

                file.write(f"SOURCE: {url}\n")
                file.write("-" * 60 + "\n")
                file.write(cleaned_text + "\n\n")
                file.write("=" * 60 + "\n\n")
                word_count = len(cleaned_text.split())
                print(f"Done! Added {word_count} words.")

    print(f"\n{filename} Cleaned Successfully!")


if __name__ == "__main__":
    urls = [
        "https://ar.wikipedia.org/wiki/ذكاء_اصطناعي",
        "https://ar.wikipedia.org/wiki/معالجة_اللغات_الطبيعية",
        "https://ar.wikipedia.org/wiki/تعلم_آلي",
        "https://ar.wikipedia.org/wiki/لغة_عربية",
        "https://ar.wikipedia.org/wiki/علم_البيانات",
    ]
    save_extensive_dataset(urls)
