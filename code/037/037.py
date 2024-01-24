import pandas as pd
import matplotlib.pyplot as plt
import pyarrow.parquet as pq
from sklearn.cluster import KMeans, DBSCAN

# Sites: 'AEP', 'COMED', 'DAYTON', 'DEOK', 'DOM', 'DUQ',
#        'EKPC', 'FE', 'NI', 'PJM', 'PJME', 'PJMW'
SITE = "DEOK"
SAMPLE_SIZE=1000
STATE = 42
df = (pq
    .read_table("data/utilities.parquet")
    .to_pandas()
    .query("site == @SITE")
    .dropna()
    .sample(n=SAMPLE_SIZE, random_state=STATE)
    .set_index(['site', 'read_date']))

df = df.div(df.sum(axis=1), axis=0) * 100

EPS = 0.41
CLUSTERS = 5
kmeans = KMeans(n_clusters=CLUSTERS, random_state=STATE).fit(df)
dbscan = DBSCAN(eps=EPS, min_samples=5).fit(df)
centroids = pd.DataFrame(kmeans.cluster_centers_)
means = df.groupby(dbscan.labels_).mean()


plt.figure(figsize=(8, 8))
for _, row in centroids.iterrows():
    plt.plot(range(24), row)

plt.title(f'Load Profiles of KMean Centroids for {SITE}')
plt.xlabel('Hour of the day')
plt.ylabel('Percentage')
plt.xticks(range(24), labels=[str(i) for i in range(24)])
plt.savefig("kmeans.png")


plt.figure(figsize=(8, 8))
for _, row in means.iterrows():
    plt.plot(range(24), row)

plt.title(f'Load Profiles of DBSCAN Means for {SITE}')
plt.xlabel('Hour of the day')
plt.ylabel('Percentage')
plt.xticks(range(24), labels=[str(i) for i in range(24)])
plt.savefig("dbscan.png")
