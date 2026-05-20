"""Arabic NLP preprocessing pipeline (spaCy-based).

Public API:
    build_pipeline()  -> spacy.Language
    process(text)     -> spacy.tokens.Doc
    normalize_text(s) -> str
    clean_tokens(doc) -> list[str]
"""

from .filters import clean_tokens
from .normalize import normalize_text
from .pipeline import build_pipeline, process

__all__ = [
    "build_pipeline",
    "process",
    "normalize_text",
    "clean_tokens",
]
