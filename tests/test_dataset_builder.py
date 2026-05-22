import pytest
from pathlib import Path
from dataset_builder import build_dataset

# Pytest automatically provides a temporary directory path unique to this test.
def test_build_dataset_creates_clean_output(tmp_path):
    # Create fake input and output paths inside the temporary folder
    fake_input = tmp_path / "fake_raw.txt"
    fake_output = tmp_path / "fake_clean.txt"

    # Write some dirty test data into our fake input file
    fake_input.write_text("   مدرسة الذكاء الاصطناعي (AI)   \n\n  سطر فارغ", encoding="utf-8")

    # Run the builder using our fake paths
    build_dataset(fake_input, fake_output)

    # Check if the builder successfully created the output file
    assert fake_output.exists() is True

    # Read the output and check if the pipeline logic was applied
    results = fake_output.read_text(encoding="utf-8").splitlines()

    # Expected: "مدرسه الذكاء الاصطناعي", empty line skipped, "سطر فارغ"
    assert len(results) == 2 
    assert "مدرسه" in results[0]  # Taa marbuta folded
    assert "(AI)" not in results[0] # English stripped
