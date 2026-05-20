"""Arabic stopword handling for the spaCy pipeline.

spaCy ships an Arabic stopword list at `spacy.lang.ar.stop_words.STOP_WORDS`.
This module applies that list (plus any project-specific extras) to a pipeline.
"""

from spacy.lang.ar.stop_words import STOP_WORDS as SPACY_AR_STOPWORDS
from spacy.language import Language

EXTRA_STOPWORDS: set[str] = set()


def apply_stopwords(nlp: Language, extra: set[str] | None = None) -> Language:
    """Flip `is_stop=True` on every Arabic stopword in the pipeline's vocab."""
    words = set(SPACY_AR_STOPWORDS) | EXTRA_STOPWORDS | (extra or set())
    for word in words:
        nlp.vocab[word].is_stop = True
    return nlp
