import pytest
from pipeline.normalize import normalize_text

@pytest.mark.parametrize("raw_input, expected_output", [
    # Test Case 1: Normalize Alif variants
    ("إأآ", "ااا"),

    # Test Case 2: Taa Marbuta to Haa
    ("مدرسة", "مدرسه"),

    # Test Case 3: Tashkeel removal
    ("تَشْكِيل", "تشكيل"),

    # Test Case 4: Tatweel removal
    ("تطويـــــل", "تطويل"),

    # Test Case 5: Complex combination (Alif, Taa Marbuta, Tashkeel, Spaces)
    ("  أَلذَّكَاءُ الإِصْطِنَاعِيَّة   ", "الذكاء الاصطناعيه"),
])
def test_normalize_text(raw_input, expected_output):
    assert normalize_text(raw_input) == expected_output
