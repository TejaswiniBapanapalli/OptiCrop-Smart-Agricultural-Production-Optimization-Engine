# univariate_analysis.py
# OptiCrop: Smart Agricultural Production Optimization Engine
# This script performs univariate analysis on agricultural dataset features.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# Set matplotlib style
plt.style.use("fivethirtyeight")

# Define numerical features to analyze
numerical_features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Create subplots for numerical features
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(14, 12))
axes = axes.flatten()  # Flatten axes for easy iteration

# Plot distribution for each numerical feature
for i, feature in enumerate(numerical_features):
    sns.histplot(data[feature], kde=True, ax=axes[i], color="skyblue")
    axes[i].set_title(f"Distribution of {feature}", fontsize=12)
    axes[i].set_xlabel(feature, fontsize=10)
    axes[i].set_ylabel("Frequency", fontsize=10)

# Remove the last empty subplot (since we have 7 features but 8 subplots)
fig.delaxes(axes[-1])

# Add overall figure title
fig.suptitle("Distribution of Agricultural Conditions", fontsize=16, weight="bold")

# Create a new figure for crop label countplot
plt.figure(figsize=(12, 6))
sns.countplot(x="label", data=data, palette="viridis")
plt.title("Count of Crop Labels", fontsize=14, weight="bold")
plt.xlabel("Crop Label", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45)

# Display all plots
plt.show()
