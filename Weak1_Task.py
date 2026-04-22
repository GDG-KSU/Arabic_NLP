import pandas as pd
import re

df = pd.read_csv("data.csv", index_col="Name", encoding='utf-8-sig')
df.index = df.index.str.strip()
df.columns = df.columns.str.strip()

df.index = [re.sub(r'\d+', '', str(name)) for name in df.index]

emp = input("Enter an employee name: ").strip()

try:
    print(df.loc[emp])
except KeyError:
    print("Employee not found", "\n")

print('-' * 30)

df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
empAge = df[df["Age"] > 20]

print(empAge)
print('-' * 30)         

print("The Youngest Employee age: ", df["Age"].min())
print("The number of employee: ", len(df))
print('-' * 30)

df.drop(columns=["Hobby"], inplace=True, errors='ignore')
df = df.dropna(subset=["Age"])

if "Phone" in df.columns:
    df["Phone"] = df["Phone"].fillna("None")
    df["Phone"] = df["Phone"].apply(lambda x: re.sub(r'\D', '', str(x)) if x != "None" else x)

df["Age"] = df["Age"].replace({30: 31})

df.to_csv("cleaned_data.csv", encoding='utf-8-sig')

print(df)

