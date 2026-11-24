
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load dataset
iris = load_iris()
X = iris.data

# Take input
k = int(input("Enter number of clusters: "))

# Apply K-Means
model = KMeans(n_clusters=k, random_state=42, n_init=10)
model.fit(X)

# Get labels
labels = model.labels_

print("Cluster labels:")
print(labels)

print("Cluster centers:")
print(model.cluster_centers_)

# Display graph
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering")
plt.show()


#installation: python -m pip install matplotlib scikit-learn