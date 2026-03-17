#Assignment (28/02/2026)
#Assignment Name : Storytelling with Graphs
#Description : Create bar chart, pie chart, histogram and write a short data story explaining trends.


import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset (using a sample dataset from seaborn for demonstration)
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# Bar Chart: Average sepal length for each species
average_sepal_length = df.groupby('species')['sepal_length'].mean()
average_sepal_length.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.xticks(rotation=0)
plt.show()
# Pie Chart: Proportion of each species in the dataset
species_counts = df['species'].value_counts()
species_counts.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'orange', 'green'])
plt.title('Proportion of Each Species')
plt.ylabel('')
plt.show()
# Histogram: Distribution of petal length
plt.hist(df['petal_length'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()  
# Data Story:
# The bar chart reveals that the average sepal length varies among the three species, with virgin   
# having the longest average sepal length, followed by versicolor and setosa. 
# The pie chart illustrates that the dataset is perfectly balanced, with each species representing 33.3% of the total samples. 
# The histogram of petal length shows a bimodal distribution, indicating that there are two distinct groups within the dataset, which correspond to the different species. 
# This suggests that petal length is a key feature for distinguishing between the species in the iris dataset.
