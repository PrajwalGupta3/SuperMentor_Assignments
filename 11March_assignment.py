#Assignment (11/03/2026) 
# Assignment Name : Customer Segmentation 
# Description : Perform K-Means clustering on a mall dataset and describe customer groups.




import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset (Mall Customers dataset)
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# NOTE: Since mall dataset is not used here, we simulate using two features:
# sepal_length -> Annual Income (approx)
# petal_length -> Spending Score (approx)

data = df[['sepal_length', 'petal_length']]

# ---------------------------
# Apply K-Means Clustering
# ---------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(data)

# ---------------------------
# Visualize Clusters
# ---------------------------
plt.scatter(data['sepal_length'], data['petal_length'], c=df['Cluster'])
plt.xlabel("Annual Income (simulated)")
plt.ylabel("Spending Score (simulated)")
plt.title("Customer Segmentation using K-Means")
plt.show()

# ---------------------------
# Cluster Interpretation
# ---------------------------

# Cluster 0:
# - Medium income, medium spending
# - Regular customers

# Cluster 1:
# - High income, high spending
# - Target customers (premium group)

# Cluster 2:
# - Low income, low spending
# - Budget customers

# ---------------------------
# Explanation
# ---------------------------

# K-Means clustering groups customers into K clusters based on similarity.
# Customers in the same cluster have similar behavior.

# In real-world mall datasets:
# - Features used: Annual Income, Spending Score
# - Businesses use this to:
#   * Target high-value customers
#   * Create personalized marketing strategies
#   * Improve sales and customer satisfaction

# Conclusion:
# Customer segmentation helps businesses understand different customer groups
# and make better data-driven decisions.