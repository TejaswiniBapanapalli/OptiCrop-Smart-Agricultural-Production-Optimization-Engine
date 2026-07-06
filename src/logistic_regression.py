# logistic_regression.py
# Project: OptiCrop - Smart Agricultural Production Optimization Engine

# Step 1: Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load the dataset
# The dataset is assumed to be located at data/Crop_recommendation.csv
data = pd.read_csv("data/Crop_recommendation.csv")

# Step 3: Separate features (X) and target (y)
X = data.drop("label", axis=1)  # All columns except 'label'
y = data["label"]               # The 'label' column

# Step 4: Split the dataset into training and testing sets
# test_size = 0.2 means 20% of the data will be used for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Scale the feature values using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on training data and transform
X_test_scaled = scaler.transform(X_test)        # Transform test data using same scaler

# Step 6: Train a Logistic Regression model
log_reg_model = LogisticRegression(
    max_iter=1000, random_state=42
)
log_reg_model.fit(X_train_scaled, y_train)

# Step 7: Predict the test data
y_pred = log_reg_model.predict(X_test_scaled)

# Step 8: Print evaluation metrics
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
