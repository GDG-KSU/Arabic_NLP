import pytest
import spacy
from pipeline.stopwords import apply_stopwords

# A fixture is a setup function, so instead of writing `spacy.blank("ar")` 
# inside every single test, we create it once here 
@pytest.fixture
def blank_nlp():
    """Provides a fresh, blank Arabic spaCy model for each test."""
    return spacy.blank("ar")

def test_default_stopwords_are_applied(blank_nlp):
    # 'في' is a standard Arabic stopword
    nlp = apply_stopwords(blank_nlp)
    assert nlp.vocab["في"].is_stop is True
    assert nlp.vocab["من"].is_stop is True

def test_extra_stopwords_are_applied(blank_nlp):
    # 'جامعة' is not a standard stopword
    # we'll prove it is false before we run our function
    assert blank_nlp.vocab["جامعة"].is_stop is False

    # Now run our function and pass 'جامعة' as an extra stopword
    nlp = apply_stopwords(blank_nlp, extra={"جامعة"})

    # Check that our function successfully mutated this specific word
    assert nlp.vocab["جامعة"].is_stop is True

def test_normal_words_are_untouched(blank_nlp):
    # 'الذكاء' is a noun, not a stopword
    nlp = apply_stopwords(blank_nlp)

    # Check that our function didn't accidentally flag everything as a stopword
    assert nlp.vocab["الذكاء"].is_stop is False
