import pandas as pd


human_file = 'Labeled_data/final_arabic_nlp_dataset.csv'
auto_file = 'Labeled_data/complete_9700_arabic_dataset.csv'

# 2. Load the datasets
human_df = pd.read_csv(human_file, encoding='utf-8-sig')
auto_df = pd.read_csv(auto_file, encoding='utf-8-sig')

print(f"📊 Loaded Human Dataset: {len(human_df)} rows")
print(f"📊 Loaded Automated Dataset: {len(auto_df)} rows")

# 3. Delete the first 716 rows from the automated dataset

auto_df_sliced = auto_df.iloc[716:]
print(f"✂️ Removed the first 716 rows from the automated dataset.")
print(f"📉 Remaining automated rows: {len(auto_df_sliced)}")

# 4. Combine the datasets (Human data first, followed by the remaining auto data)
final_combined_df = pd.concat([human_df, auto_df_sliced], axis=0, ignore_index=True)

# 5. Save the new hybrid dataset
output_filename = 'final_hybrid_dataset_10k.csv'
final_combined_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print("\n" + "="*40)
print(f"🎉 Data successfully replaced and merged!")
print(f"📂 Output saved as: {output_filename}")
print(f"📈 Total rows in new dataset: {len(final_combined_df)}")
print("="*40)