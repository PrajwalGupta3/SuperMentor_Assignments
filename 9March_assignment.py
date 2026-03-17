#Assignment (09/03/2026)
#Assignment Name : House Price Predictor
#Description : Train a Linear Regression model, predict prices, and test with new input.




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

# Select features and target
features = df[['carat', 'depth', 'table', 'x', 'y', 'z']]
target = df['price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# ---------------------------
# Model Evaluation
# ---------------------------
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Evaluation:")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# ---------------------------
# Test with New Input
# ---------------------------
new_input = pd.DataFrame([[0.5, 61.5, 55, 5.1, 5.1, 3.1]],
                         columns=['carat', 'depth', 'table', 'x', 'y', 'z'])

predicted_price = model.predict(new_input)

print("\nPredicted Price for New Input:")
print(predicted_price)
# The model predicts the price of a diamond based on its features such as carat, depth, table, and dimensions (x, y, z).
