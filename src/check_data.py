import pandas as pd

# 1. Update the extension to .parquet
file_path = "data/processed/Cleaned_Dataset.parquet"

print("Loading Parquet dataset...")

# 2. Stripped out all CSV text-parsing arguments. 
# Parquet handles schemas natively.
df = pd.read_parquet(file_path, engine="pyarrow")

# 1. Basic Statistics
print("\n" + "="*40)
print("📊 DATASET PROFILE")
print("="*40)
print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print(f"Column Names: {list(df.columns)}")

# 2. Check for missing or broken data
null_counts = df.isnull().sum()
print("\n⚠️ NULL VALUES CHECK:")
print(null_counts)

# 3. Visual Sanity Check (Read random rows)
print("\n" + "="*40)
print("👀 RANDOM SAMPLE (3 Rows)")
print("="*40)
# Ensure your text column is actually named 'text'
samples = df.sample(3)
for index, row in samples.iterrows():
    print(f"Row {index}:")
    print(row['text'])
    print("-" * 40)
