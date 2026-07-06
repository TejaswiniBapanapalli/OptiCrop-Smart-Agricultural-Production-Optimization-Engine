import pandas as pd

# Load dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# Dataset Shape
print("Dataset Shape:")
print(data.shape)

# Dataset Information
print("\nDataset Information:")
data.info()

# Data Types
print("\nData Types:")
print(data.dtypes)

# Check Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Final Status
if data.isnull().sum().sum() == 0:
    print("\n✅ No missing values found.")
    print("Dataset is clean and ready for preprocessing.")
else:
    print("\n⚠ Missing values detected.")
    print("Handle missing values before model training.")