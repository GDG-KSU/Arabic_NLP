# GDSC KSU: Arabic NLP Open Source Project

The Arabic NLP ecosystem currently faces a significant gap, particularly regarding open source datasets and models evaluated on local dialects. We aim to bridge the gap by providing high quality datasets to the Arabic technical community.

##  Project Overview
We aspire to build a foundation for Arabic AI datasets, by collecting, cleaning, and publishing robust datasets, we aim to accelerate the development of AI applications that serve Arabic speakers. 

All our datasets are to be published on [HuggingFace Hub](https://huggingface.co/) and GitHub.

## Who is this for?
- **Primary:** Arabic NLP researchers and developers needing Arabic datasets.
- **Community:** The broader HuggingFace and GitHub Arabic tech community.

## Technical Setup & Usage
This repository utilizes a modular, `spaCy`-driven NLP pipeline to ingest raw data, normalize Arabic text, filter stopwords, and output ML-ready Parquet files.

### 1. Prerequisites
Ensure you have **Python 3.10+** installed. We highly recommend using a Virtual Environment.

### 2. Installation
Create your virtual environment and install the required dependencies:
```bash
python -m venv venv
# Activate the venv (Windows: .\venv\Scripts\activate | Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```
