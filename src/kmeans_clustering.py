# kmeans_clustering.py
# Project: OptiCrop - Smart Agricultural Production Optimization Engine

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Load the dataset
# The dataset is assumed to be located at data/Crop_recommendation.csv
data = pd.read_csv("data/Crop_recommendation.csv")

# Step 2: Separate features (X) and target (y)
X = data.drop("label", axis=1)  # All columns except 'label'
y = data["label"]               # The 'label' column

# Step 3: Implement the Elbow Method
wcss = []  # List to store Within-Cluster Sum of Squares
for i in range(1, 11):  # Testing cluster values from 1 to 10
    kmeans = KMeans(
        n_clusters=i,
        init="k-means++",
        max_iter=300,
        n_init=10,
        random_state=42
    )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  # Inertia is the WCSS value

# Step 4: Plot the Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker="o", linestyle="--", color="b")
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS (Within-Cluster Sum of Squares)")
plt.grid(True)
plt.show()

# Step 5: Train the KMeans model with chosen parameters
kmeans_model = KMeans(
    n_clusters=4,
    init="k-means++",
    max_iter=300,
    n_init=10,
    random_state=42
)
clusters = kmeans_model.fit_predict(X)  # Predict cluster labels

# Step 6: Create a DataFrame with Cluster and Crop Label
clustered_data = pd.DataFrame({
    "Cluster": clusters,
    "Crop Label": y
})

# Step 7: Print unique crops in each cluster
for cluster_num in range(4):
    crops_in_cluster = clustered_data[clustered_data["Cluster"] == cluster_num]["Crop Label"].unique()
    print(f"\nUnique crops in Cluster {cluster_num}:")
    print(crops_in_cluster)
