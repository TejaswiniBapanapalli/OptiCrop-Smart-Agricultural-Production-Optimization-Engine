# outlier_detection.py
# -----------------------------------------------------------
# OptiCrop: Smart Agricultural Production Optimization Engine
# Outlier Detection Script
#
# This script performs outlier detection and removal using the
# Interquartile Range (IQR) method on the Crop Recommendation dataset.
# -----------------------------------------------------------

# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the dataset
data_path = "data/Crop_recommendation.csv"
df = pd.read_csv(data_path)

# 3. Display boxplots for all numerical columns before outlier removal
numerical_features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

plt.figure(figsize=(15, 10))
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df[feature], color="skyblue")
    plt.title(f"Boxplot of {feature} (Before Outlier Removal)")
plt.tight_layout()
plt.show()

# 4. Calculate IQR for each numerical feature
Q1 = df[numerical_features].quantile(0.25)
Q3 = df[numerical_features].quantile(0.75)
IQR = Q3 - Q1

# 5. Calculate Lower Bound and Upper Bound
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 6. Remove outliers using the IQR method
print("Dataset shape before outlier removal:", df.shape)

# Keep only rows within bounds for all numerical features
df_clean = df[~((df[numerical_features] < lower_bound) | (df[numerical_features] > upper_bound)).any(axis=1)]

print("Dataset shape after outlier removal:", df_clean.shape)

# 7. Display boxplots after outlier removal
plt.figure(figsize=(15, 10))
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df_clean[feature], color="lightgreen")
    plt.title(f"Boxplot of {feature} (After Outlier Removal)")
plt.tight_layout()
plt.show()

# 8. Print completion message
print("✅ Outlier detection and removal is complete.")
