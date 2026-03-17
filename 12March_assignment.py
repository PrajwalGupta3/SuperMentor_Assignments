#Assignment (12/03/2026)
# Assignment Name : Decision Tree on Paper
# Description : Draw a decision tree predicting whether you should play outside.



# Assignment: Decision Tree on Paper
# Problem: Predict whether to play outside

# We build a simple decision tree using factors like:
# - Weather (Sunny, Rainy, Cloudy)
# - Temperature (Hot, Mild, Cool)
# - Humidity (High, Normal)

# ---------------------------
# Decision Tree Structure
# ---------------------------

#                Weather
#               /   |    \
#           Sunny Rainy Cloudy
#            /        |       \
#     Humidity     (No)      (Yes)
#       /    \
#    High   Normal
#    (No)    (Yes)

# ---------------------------
# Explanation
# ---------------------------

# Step 1: Check Weather
# - If Weather = Rainy → Do NOT play (ground may be wet)
# - If Weather = Cloudy → Play (pleasant conditions)
# - If Weather = Sunny → Check Humidity

# Step 2: Check Humidity (only if Sunny)
# - If Humidity = High → Do NOT play (too sweaty/uncomfortable)
# - If Humidity = Normal → Play

# ---------------------------
# Example Predictions
# ---------------------------

# Example 1:
# Weather = Sunny, Humidity = High → Output: No

# Example 2:
# Weather = Cloudy → Output: Yes

# Example 3:
# Weather = Rainy → Output: No

# ---------------------------
# Conclusion
# ---------------------------

# A decision tree makes decisions step-by-step using conditions.
# It is easy to understand and visually interpret.
# Widely used in classification problems in machine learning.