"""Build a configured spaCy pipeline for Arabic preprocessing."""

import spacy
from spacy.language import Language

from .normalize import arabic_normalizer, normalize_text  # noqa: F401
from .stopwords import apply_stopwords


def build_pipeline(extra_stopwords: set[str] | None = None) -> Language:
    """Return a blank Arabic spaCy pipeline with normalization + stopwords."""
    nlp = spacy.blank("ar")
    nlp.add_pipe("arabic_normalizer", last=True)
    apply_stopwords(nlp, extra=extra_stopwords)
    return nlp


def process(text: str, nlp: Language | None = None):
    """Convenience: normalize raw text, then run through the pipeline."""
    nlp = nlp or build_pipeline()
    return nlp(normalize_text(text))
