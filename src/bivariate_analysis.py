# bivariate_analysis.py
# OptiCrop: Smart Agricultural Production Optimization Engine
# -----------------------------------------------------------
# This script performs bivariate analysis of key agricultural features
# against crop labels using scatter plots.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# Set matplotlib style
plt.style.use("fivethirtyeight")

# Define features to analyze
features = ["humidity", "temperature", "rainfall", "ph", "N", "P", "K"]

# Create subplots (2 rows × 4 columns)
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
axes = axes.flatten()  # Flatten to easily iterate over

# Generate scatter plots for each feature vs crop label
for i, feature in enumerate(features):
    sns.scatterplot(
        x=feature,
        y="label",
        data=data,
        ax=axes[i],
        hue="label",  # Different colors for crop labels
        palette="Set2",
        legend=False
    )
    axes[i].set_title(f"{feature.capitalize()} vs Crop Label")
    axes[i].set_xlabel(feature.capitalize())
    axes[i].set_ylabel("Crop Label")

# Hide the last empty subplot (since we have 7 plots, not 8)
fig.delaxes(axes[-1])

# Add main title
fig.suptitle("Bivariate Analysis of Agricultural Features", fontsize=16, fontweight="bold")

# Adjust layout for neatness
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Display plots
plt.show()
