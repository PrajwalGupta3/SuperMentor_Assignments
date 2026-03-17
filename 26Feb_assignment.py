#Assignment (26/02/2026)
#Assignment Name : Data Doctor
#Description : Clean a dataset by handling missing values, removing duplicates, standardizing text, and explain why cleaning matters.



import pandas as pd

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Display basic info before cleaning
print("Original Dataset:")
print(df.head())
print("\nShape before cleaning:", df.shape)

# ---------------------------
# 1. Handle Missing Values
# ---------------------------
# Fill numeric columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# ---------------------------
# 2. Remove Duplicates
# ---------------------------
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)

df.drop_duplicates(inplace=True)

# ---------------------------
# 3. Standardize Text
# ---------------------------
df['species'] = df['species'].str.lower().str.strip()

# ---------------------------
# Final Output
# ---------------------------
print("\nCleaned Dataset:")
print(df.head())
print("\nShape after cleaning:", df.shape)

