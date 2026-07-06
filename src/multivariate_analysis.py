# multivariate_analysis.py
# OptiCrop: Smart Agricultural Production Optimization Engine
# -----------------------------------------------------------
# This script performs multivariate analysis of agricultural features
# using correlation heatmaps and pairplots.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/Crop_recommendation.csv")

# Set matplotlib style
plt.style.use("fivethirtyeight")

# -----------------------------------------------------------
# Correlation Heatmap
# -----------------------------------------------------------
# Compute correlation matrix for numerical features
corr_matrix = data[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]].corr()

# Create heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    corr_matrix,
    annot=True,          # Show correlation values
    cmap="coolwarm",     # Color palette
    fmt=".2f",           # Format values to 2 decimal places
    linewidths=0.5
)
plt.title("Correlation Heatmap of Agricultural Features", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# Pairplot Analysis
# -----------------------------------------------------------
# Create pairplot for selected features colored by crop label
sns.pairplot(
    data,
    vars=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
    hue="label",          # Color by crop label
    palette="Set2",
    diag_kind="kde"       # Kernel density estimate on diagonals
)

# Add title to pairplot
plt.suptitle("Pairplot of Agricultural Features by Crop Label", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()
