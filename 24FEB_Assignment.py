#Assignment (24/02/2026)

#Assignment Name : Dataset Detective
#Description : Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.
import pandas as pd
# Load the dataset (using a sample dataset from seaborn for demonstration)
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# Display the top rows of the dataset
print(df.head())
# Find the column with the highest average value (for numeric columns)
numeric_cols = df.select_dtypes(include='number')
column_averages = numeric_cols.mean()
highest_avg_column = column_averages.idxmax()
print(f"Column with highest average value: {highest_avg_column}")
print(f"Highest average value: {column_averages[highest_avg_column]}")
# Count missing values in the dataset
missing_values_count = df.isnull().sum()
print("Missing values in each column:")
print(missing_values_count)
# Insights:
# 1. The dataset contains 150 rows and 5 columns, with no missing values    
# 2. The 'sepal_length' column has the highest average value among the numeric columns.
# 3. The dataset is balanced with 50 samples for each of the three species (setosa, versicolor, virginica).
# 4. The 'sepal_length' and 'sepal_width' columns show a positive correlation, while 'petal_length' and 'petal_width' show a stronger positive correlation.
# 5. The dataset is commonly used for classification tasks in machine learning, particularly for testing algorithms on multi-class classification problems.