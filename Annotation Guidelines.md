# 📖 Annotation & Preprocessing Guidelines
> **Project:** Arabic NLP Dataset Construction  
> **Phase:** 3 (Dataset)  

## 1. Introduction
These guidelines establish the standard procedures for cleaning and normalizing Modern Standard Arabic text scraped from technical and encyclopedic web sources. Adhering to these rules ensures consistency and high data quality for downstream Machine Learning and NLP tasks.

## 2. Text Cleaning Standards
The scraping script (`Dataset.py`) is designed to process raw text according to the following criteria:

### A. Language Filtering
* **Arabic-Only Corpus:** The dataset must only contain Arabic characters and whitespaces.
* **Non-Arabic Removal:** All Latin characters (A-Z, a-z), English numerals, and special symbols are stripped.
* **Reason:** To minimize Out-of-Vocabulary issues and focus the model strictly on Arabic linguistic patterns.

### B. Noise & Artifact Removal
* **URL Stripping:** Hyperlinks and web addresses are removed.
* **Citation Cleanup:** Wikipedia-style references (e.g., [1], [2]) are deleted.
* **Symbol Removal:** Special characters such as (@, #, $, %) and punctuation that do not contribute to semantic meaning are removed.

## 3. Orthographic Normalization
To reduce vocabulary sparsity, specific characters are normalized to a uniform base form:

| Original Character(s) | Normalized Form | Rule Description |
| :--- | :--- | :--- |
| **أ / إ / آ** | **ا** | Convert all أ forms (Hamza above/below, Madda) to 'ا' . |
| **ة** | **ه** | Normalize 'ة' to 'ه '. |
| **Tashkeel (Diacritics)** | **(None)** | Complete removal of all diacritics ( َ ,  ُ ,  ِ , etc.). |

## 4. Formatting & Structure
* **Paragraph Preservation:** Each line in the output file represents a single cohesive paragraph to maintain context.
* **Space Normalization:** Multiple consecutive whitespaces are collapsed into a single space.
* **Encoding:** Files are saved using **UTF-8** encoding to prevent character corruption.

## 5. Examples
| Input Text | Processed Output |
| :--- | :--- |
| "الذكاء الاصطناعي (AI) [1] هو فَرعٌ..." | "الذكاء الاصطناعي هو فرع" |
| "تعلّمُ الآلةِ يغيّر العالم!" | "تعلم اله يغير العالم" |

---
**Author:** Ghadah Basalasel
**Date:** May 2026