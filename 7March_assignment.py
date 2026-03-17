#Assignment (07/03/2026)
#Assignment Name : KNN in Real Life
#Description : Explain Netflix-like recommendations using KNN and create a small similarity example.




# Assignment: KNN in Real Life (Netflix-like Recommendations)

# 1. Explanation: How KNN is used in recommendations (like Netflix)

# K-Nearest Neighbors (KNN) is used to recommend items based on similarity.
# In platforms like Netflix, the system finds users or movies that are similar.

# There are two main approaches:
# - User-Based KNN:
#   * Find users with similar watching preferences
#   * Recommend movies that similar users liked

# - Item-Based KNN:
#   * Find movies similar to the one a user liked
#   * Recommend those similar movies

# Example:
# If User A and User B both liked Action and Thriller movies,
# and User A watched a new movie, that movie can be recommended to User B.

# KNN works by:
# 1. Calculating similarity (distance) between users/items
# 2. Selecting K nearest neighbors (most similar ones)
# 3. Recommending based on their preferences


# 2. Small Similarity Example

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example: Movie ratings by users
# Rows = Users, Columns = Movies
# (Ratings out of 5)

ratings = np.array([
    [5, 4, 0, 0],  # User 1
    [4, 5, 0, 0],  # User 2
    [0, 0, 5, 4],  # User 3
])

# Calculate similarity between users
similarity_matrix = cosine_similarity(ratings)

print("User Similarity Matrix:")
print(similarity_matrix)


# 3. Interpretation

# - User 1 and User 2 will have high similarity (similar tastes)
# - User 3 is very different (likes different movies)

# Recommendation Idea:
# If User 1 watches a new movie, recommend it to User 2
# because they are similar users.


# Conclusion:
# KNN helps recommendation systems by finding similar users or items.
# It is simple, effective, and widely used in real-world platforms like Netflix.