"""Post-pipeline token cleaning."""

from spacy.tokens import Doc


def clean_tokens(doc: Doc) -> list[str]:
    """Return normalized tokens, excluding stopwords, punctuation, spaces, URLs.

    Uses token.norm_ so this is safe whether or not the caller pre-normalized
    the raw text — the arabic_normalizer component fills norm_ either way.
    """
    return [
        t.norm_
        for t in doc
        if not t.is_stop and not t.is_punct and not t.is_space and not t.like_url
    ]
