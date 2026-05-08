---
language:
- ar
size_categories:
- n<1K
task_categories:
- text-generation
- fill-mask
pretty_name: Arabic Technical Wiki Corpus
tags:
- arabic-nlp
- gdg-ksu
- technical-corpus
---

# Arabic Technical Wiki Corpus

## Project Overview
This dataset is a curated collection of Modern Standard Arabic text, specifically focused on technical and scientific domains such as Artificial Intelligence and Data Science. It was developed as the final deliverable of the **GDG KSU Development Program 2026**.

The goal of this project is to provide a high-quality, preprocessed Arabic corpus that can be used for NLP research, specifically for those interested in technical terminology.

## Dataset Statistics
- **Source:** Arabic Wikipedia.
- **Topics:** AI, NLP, Machine Learning, Arabic Language, Data Science.
- **Size Category:** `n<1K` (Small-scale curated dataset).
- **Format:** Cleaned Plain Text (.txt) encoded in UTF-8.
- **Word Count:** 4300

## Preprocessing Methodology
To ensure the dataset is ready for Machine Learning tasks, a rigorous cleaning pipeline was implemented using `PyArabic` and `Regex`:

1.  **Normalization:**
    * Unified all ' ا ' forms (أ، إ، آ) into (ا).
    * Normalized (ة) into (ه).
2.  **Noise Removal:**
    * Removed all Latin characters, symbols, and Wikipedia citations.
    * Stripped all URLs and web links.
3.  **Tashkeel Removal:**
    * Used `araby.strip_tashkeel` to remove all Arabic diacritics for better model performance.
4.  **Whitespace Cleaning:**
    * Unified multi-spaces into a single space and trimmed the text.

## File Structure
- `Dataset.py`: The Python engine used for scraping and cleaning.
- `Cleaned_Dataset.txt`: The final processed text data.
- `Dataset_README.md`: The official Dataset Card and documentation.

## Technical Setup & Usage
To replicate this dataset or run the scraper locally, follow these steps:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. You will also need the following libraries:
* `requests`: To fetch the web pages.
* `beautifulsoup4`: To parse the HTML content.
* `pyarabic`: To perform Arabic text normalization and cleaning.

### 2. Installation
Install the required dependencies using pip:
```bash
pip install requests beautifulsoup4 pyarabic

## Author
**Ghadah Basalasel** *Third-year Information Systems Student at King Saud University* *Dataset Collection & Cleaning Contributor — Arabic NLP Track (m6)* *Robot Programmer & Software Developer*

---
*This project was developed as part of the **GDG KSU Development Program 2026**.*