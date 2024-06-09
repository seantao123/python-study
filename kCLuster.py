# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generating random data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Creating a KMeans instance
kmeans = KMeans(n_clusters=4)

# Fitting the KMeans model to the data
kmeans.fit(X)

# Getting the cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting the data points and cluster centers
plt.figure(figsize=(8, 6))

# Plotting the data points
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7, edgecolors='k')

# Plotting the cluster centers
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.8, marker='X')

plt.title('KMeans Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()
