import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# Features and Target
X = data.drop("label", axis=1)
y = data["label"]

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining and Testing Dataset Shapes")

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)

print("\n✅ Train-Test Split completed successfully.")