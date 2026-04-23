import pandas as pd
import re

try:
    df = pd.read_csv("data.csv", index_col="Name", encoding="utf-8-sig")
except FileNotFoundError:
    print("Error: 'data.csv' file not found!")
    exit()

df.index = df.index.str.strip()
df.columns = df.columns.str.strip()

df.index = [re.sub(r"\d+", "", str(name)).strip() for name in df.index]

emp = input("Enter an employee name to search: ").strip()
print("-" * 30)

try:
    print(f"Details for {emp}:")
    print(df.loc[emp])
except KeyError:
    print(f"Result: Employee '{emp}' not found.")

print("-" * 30)

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

emp_age = df[df["Age"] > 20]
print("Employees older than 20:")
print(emp_age, "\n")

print(f"The Youngest Employee age: {df['Age'].min()}")
print(f"Total number of employees: {len(df)}\n")

df.drop(columns=["Hobby"], inplace=True, errors="ignore")
df = df.dropna(subset=["Age"])

if "Phone" in df.columns:
    df["Phone"] = df["Phone"].fillna("None")
    df["Phone"] = df["Phone"].apply(
        lambda x: re.sub(r"\D", "", str(x)) if x != "None" else x
    )

df["Age"] = df["Age"].replace({30: 31})

df.to_csv("cleaned_data.csv", encoding="utf-8-sig")

print("Final Cleaned Data:")
print(df)
