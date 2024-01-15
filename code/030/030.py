from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import pandas as pd

X, y = make_blobs(
    n_samples=300, 
    centers=3, 
    random_state=12)

model = DBSCAN(eps=0.7, min_samples=5)
labels = model.fit_predict(X)
data = pd.DataFrame(
    {'Feature1': X[:, 0], 'Feature2': X[:, 1], 
    'TrueLabel': y, 'ClusterLabel': labels})

plt.figure(figsize=(8, 6))
plt.scatter(
    data['Feature1'], 
    data['Feature2'], 
    c=data['ClusterLabel'], 
    cmap='Dark2')
plt.title('DBSCAN Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.savefig("clusters.png")
