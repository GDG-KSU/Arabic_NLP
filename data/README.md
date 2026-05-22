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
- **Format:** Parquet (`.parquet`) - Columnar storage for optimized reading.
- **Word Count:** ~4300

## Preprocessing Methodology
To ensure the dataset is ready for Machine Learning tasks, a rigorous, modular cleaning pipeline was implemented using `spaCy`, `PyArabic`, and `Regex`. The data passes through the following orchestrated steps:

1.  **Orthographic Normalization:**
    * Unified all ' ا ' forms (أ، إ، آ) into bare (ا).
    * Folded Taa Marbuta (ة) into Haa (ه).
    * Converted Arabic-Indic digits to standard ASCII digits.
2.  **Noise & Artifact Removal:**
    * Removed all Latin characters, English numerals, symbols, and Wikipedia citations.
    * Stripped all URLs and web links.
3.  **Tashkeel & Tatweel Removal:**
    * Used `araby.strip_tashkeel` to remove all Arabic diacritics.
    * Removed Tatweel (ـ) extension characters.
4.  **Token Filtering (spaCy):**
    * Applied custom stopword filtering via the spaCy vocabulary.
    * Dropped residual punctuation and whitespace tokens.

## File Structure
The data processing architecture is modularized for CI/CD integration:
- `data/raw/`: Contains the original scraped text.
- `data/processed/Cleaned_Dataset.parquet`: The final, optimized dataset.
- `src/pipeline/`: The custom spaCy NLP package (handles normalization, filtering, and stopwords).
- `src/dataset_builder.py`: The orchestration script that pushes raw data through the pipeline.
- `tests/`: Pytest suite ensuring data and pipeline integrity.

## Author
**Ghadah Basalasel** *Third-year Information Systems Student at King Saud University* *Dataset Collection & Cleaning Contributor — Arabic NLP Track (m6)* *Robot Programmer & Software Developer*

---
*This project was developed as part of the **GDG KSU Development Program 2026**.*