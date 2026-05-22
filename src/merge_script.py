import glob
import os

import pandas as pd

folder_path = "Labeled_data"
file_pattern = os.path.join(folder_path, "*.csv")

all_files = glob.glob(file_pattern)
data_frames_list = []

print(f"📊 Found {len(all_files)} files to merge...")

for file_path in all_files:
    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")

        if not df.empty:
            data_frames_list.append(df)
            print(
                f"✅ Successfully read: {os.path.basename(file_path)} | Rows: {len(df)}"
            )
        else:
            print(
                f"⚠️ Warning: The file {os.path.basename(file_path)} is empty and was skipped."
            )

    except Exception as e:
        print(f"❌ Error reading file {os.path.basename(file_path)}: {e}")

if data_frames_list:
    combined_df = pd.concat(data_frames_list, axis=0, ignore_index=True)
    combined_df = combined_df.dropna(subset=["text"])

    output_filename = "final_arabic_nlp_dataset.csv"
    combined_df.to_csv(output_filename, index=False, encoding="utf-8-sig")

    print("\n" + "=" * 40)
    print("🎉 Dataset merged successfully into a single file!")
    print(f"📂 Output filename: {output_filename}")
    print(f"📈 Total rows in combined dataset: {len(combined_df)}")
    print(f"📋 Columns in the merged file: {list(combined_df.columns)}")
    print("=" * 40)
else:
    print("\n❌ No files were merged. Please check the folder path.")
    