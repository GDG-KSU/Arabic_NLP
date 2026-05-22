import pytest
import spacy

from pipeline.filters import clean_tokens


@pytest.fixture
def blank_nlp():
    return spacy.blank("ar")


def test_clean_tokens_removes_unwanted_types(blank_nlp):
    # 1. Setup: Create a raw Doc containing one of every type of token
    text = "مرحبا   في . https://example.com"
    doc = blank_nlp(text)

    # 2. Manipulation: Modify the Vocab (not the Token) for the stopword
    for token in doc:
        if token.text == "في":
            # CORRECT: Update the Lexeme in the central vocabulary
            doc.vocab[token.text].is_stop = True

        # We manually set norm_ to prove the filter returns norm_, not text
        token.norm_ = token.text + "_norm"

    # 3. Execution
    result = clean_tokens(doc)

    # 4. Assertion
    # Expected: "مرحبا" is the ONLY token that survives the filter.
    assert len(result) == 1
    assert result[0] == "مرحبا_norm"
