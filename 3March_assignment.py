#Assignment (03/03/2026)
#Assignment Name : Build Your First Dataset
#Description : Create a dataset (e.g., study hours vs marks), identify features & labels, predict relationship.



# Build Your First Dataset:
import pandas as pd
# Create a simple dataset of study hours vs marks
data = {
    'study_hours': [1, 2, 3, 4, 5],
    'marks': [40, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
# Display the dataset
print(df)
# Identify features and labels
features = df['study_hours']  # This is the feature (input)
labels = df['marks']  # This is the label (output)
# Predict the relationship (using a simple linear relationship for demonstration)
# Assuming a linear relationship: marks = 10 * study_hours + 30
predicted_marks = 10 * features + 30
# Display the predicted marks
print("Predicted Marks based on Study Hours:")
print(predicted_marks)
# The dataset shows a clear linear relationship between study hours and marks, where each additional hour of study is associated with an increase of 10 marks.
