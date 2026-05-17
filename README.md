# GDSC KSU: Arabic NLP Open Source Project

The Arabic NLP ecosystem currently faces a significant gap, particularly regarding open source datasets and models evaluated on local dialects. We aim to bridge the gap by providing high quality datasets to the Arabic technical community.

##  Project Overview
We aspire to build a foundation for Arabic AI datasets, by collecting, cleaning, and publishing robust datasets, we aim to accelerate the development of AI applications that serve Arabic speakers. 

All our datasets are to be published on [HuggingFace Hub](https://huggingface.co/) and GitHub.

## Who is this for?
- **Primary:** Arabic NLP researchers and developers needing Arabic datasets.
- **Community:** The broader HuggingFace and GitHub Arabic tech community.

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
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/GDG-KSU/Arabic_NLP?tab=Apache-2.0-1-ov-file#) file for details.