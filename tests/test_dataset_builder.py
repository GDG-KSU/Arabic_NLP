import pandas as pd
from dataset_builder import build_dataset

# Pytest automatically provides a temporary directory path unique to this test.
def test_build_dataset_creates_clean_output(tmp_path):
    # 1. Setup: Create fake Parquet file paths inside the temporary testing folder
    fake_input = tmp_path / "fake_raw.parquet"
    fake_output = tmp_path / "fake_clean.parquet"

    # Create a dummy dataframe mimicking your actual raw dataset
    df_raw = pd.DataFrame({
        "text": ["   مدرسة الذكاء الاصطناعي (AI)   ", "اختبار"],
        "label": ["tech", "general"],
        "annotator": ["user1", "user2"]
    })
    
    # Save the dummy data as a Parquet file using pyarrow
    df_raw.to_parquet(fake_input, engine="pyarrow", index=False)

    # 2. Execution: Run the builder (this will now bypass the .txt block and succeed)
    build_dataset(fake_input, fake_output)

    # 3. Assertion: Verify the output file was created
    assert fake_output.exists()

    # Load the cleaned Parquet file to verify data integrity
    df_clean = pd.read_parquet(fake_output, engine="pyarrow")

    # Verify the NLP pipeline was applied correctly to the 'text' column
    # Expected changes: English letters removed, parentheses removed, Taa Marbuta folded to Haa
    assert len(df_clean) == 2
    assert df_clean.iloc[0]["text"] == "مدرسه الذكاء الاصطناعي"
    assert df_clean.iloc[1]["text"] == "اختبار"
    
    # Verify the other columns were preserved
    assert "label" in df_clean.columns
    assert "annotator" in df_clean.columns
