"""Arabic text normalization."""

import re

import pyarabic.araby as araby
from spacy.language import Language
from spacy.tokens import Doc

_ALIF_VARIANTS = re.compile(r"[إأآ]")
_TAA_MARBUTA = re.compile(r"ة")
_TATWEEL = re.compile(r"ـ")
_ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")


def normalize_text(text: str) -> str:
    """Normalize raw Arabic text.

    - strip tashkeel (diacritics)
    - remove tatweel (ـ)
    - unify alif variants (إ أ آ → ا)
    - fold taa marbuta to haa (ة → ه) — matches the scraping convention
      already applied to the existing dataset
    - convert Arabic-Indic digits to ASCII
    - collapse whitespace
    """
    text = araby.strip_tashkeel(text)
    text = _TATWEEL.sub("", text)
    text = _ALIF_VARIANTS.sub("ا", text)
    text = _TAA_MARBUTA.sub("ه", text)
    text = text.translate(_ARABIC_DIGITS)
    text = re.sub(r"\s+", " ", text).strip()
    return text


@Language.component("arabic_normalizer")
def arabic_normalizer(doc: Doc) -> Doc:
    """Safety-net component: ensures token.norm_ holds the normalized form.

    Lets callers who pass un-normalized text directly to `nlp(text)` still get
    normalized output via `token.norm_`. Use `clean_tokens(doc)` downstream and
    you're safe whether or not the caller pre-normalized.
    """
    for token in doc:
        token.norm_ = normalize_text(token.text)
    return doc
