import pandas as pd

try:
    # Load dataset
    data = pd.read_csv("data/Crop_recommendation.csv")

    print("✅ Dataset Loaded Successfully\n")

    print("First 5 Records:")
    print(data.head())

    print("\nDataset Shape:")
    print(data.shape)

    print("\nColumn Names:")
    print(data.columns)

    print("\nData Types:")
    print(data.dtypes)

except FileNotFoundError:
    print("❌ Dataset not found. Please check the file path.")