#Assignment (18/03/2026)

#Assignment Name : Customer Segmentation
#Description : Perform K-Means clustering on a mall dataset and describe customer groups.


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset locally
df = pd.read_csv('18March_assignment/Mall_Customers.csv')

# Features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.show()

# KMeans
kmeans = KMeans(n_clusters=5, random_state=0, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# Plot
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y_kmeans)
plt.show()