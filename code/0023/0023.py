import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

def expectation(x, centers):
  return np.argmin(np.linalg.norm(x[:, np.newaxis] - centers, axis=2), axis=1)

def maximization(x, labels, k):
  return np.array([x[labels == i].mean(axis=0) for i in range(k)])

dim = (100, 2)
data = (np.random.normal(0, 1, dim), np.random.normal(5, 1, dim))
data = np.vstack(data)

def kmeans(X, k, max_iters=100):
    centroids = X[np.random.choice(len(X), k, replace=False)]
    for _ in range(max_iters):
        labels = expectation(X, centroids)
        new_centroids = maximization(X, labels, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return labels, centroids

# Perform K-Means clustering
labels, centroids = kmeans(data, k=2)

# Perform EM clustering (GMM)
gmm = GaussianMixture(n_components=2)
gmm.fit(data)
em_labels = gmm.predict(data)
em_means = gmm.means_

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1], c=labels, 
    cmap="Dark2", alpha=0.4, edgecolor='k')
plt.scatter(centroids[:, 0], centroids[:, 1], 
    c='#e41a1c', s=150, marker='D')
plt.title("K-Means Clustering")
plt.savefig("scatter.png")
plt.show()


plt.figure(figsize=(8, 6))
ax=plt.gca()
for cluster_label in np.unique(labels):
    sns.kdeplot(data[labels == cluster_label, 0], ax=ax, label=f'K-Means Cluster of {cluster_label}')

plt.title("K-Means Cluster Distributions on X")
plt.legend()
plt.savefig("kde-x.png")

plt.figure(figsize=(8, 6))
ax=plt.gca()
for cluster_label in np.unique(labels):
    sns.kdeplot(data[labels == cluster_label, 1], ax=ax, label=f'K-Means Cluster of {cluster_label}')

plt.title("K-Means Cluster Distributions on Y")
plt.legend()
plt.savefig("kde-y.png")
