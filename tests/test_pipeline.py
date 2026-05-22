from pipeline.pipeline import build_pipeline, process
from spacy.tokens import Doc

def test_build_pipeline_assembly():
    # Execute
    nlp = build_pipeline(extra_stopwords={"جامعة"})
    
    # Assert 1: Did it add our custom component to the spaCy pipeline?
    assert "arabic_normalizer" in nlp.pipe_names
    
    # Assert 2: Did it apply the stopwords? 
    # (Testing the integration with stopwords.py)
    assert nlp.vocab["جامعة"].is_stop is True
    assert nlp.vocab["في"].is_stop is True

def test_process_end_to_end():
    # Setup messy text
    raw_text = "   الذكاء الاصطناعي (AI) إختبار ة   "

    # Execute the master process function
    doc = process(raw_text)

    # Assert 1: It must return a spaCy Doc
    assert isinstance(doc, Doc)

    # Assert 2: The Doc's text should be the fully normalized string 
    # (checking integration with normalize.py)
    # Notice: Spaces collapsed, Alif normalized, Taa Marbuta folded.
    expected_normalized = "الذكاء الاصطناعي (AI) اختبار ه"
    assert doc.text == expected_normalized
