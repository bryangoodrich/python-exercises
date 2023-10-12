# github.com/bryangoodrich/python-exercises
# code/0016/0016.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler

base = "https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master"
dataset = "Wholesale%20Customers/Wholesale%20customers%20data.csv"
df = pd.read_csv(f"{base}/{dataset}")
df.Channel = df.Channel.replace({1: "Hotel/Restaurant/Cafe", 2: "Retail"})

k = 5
categories = ["Region", "Channel"]
numeric_columns = df.drop(categories, axis=1)
percent_annual_spend = numeric_columns.div(numeric_columns.sum(axis=1), axis=0)
featureset = StandardScaler().fit_transform(percent_annual_spend)
kmeans = KMeans(n_clusters=k, n_init="auto")
df['Cluster'] = kmeans.fit_predict(featureset)
df.groupby(categories + ['Cluster']).size().unstack().fillna(0)
# Cluster                          0     1     2     3     4
# Region Channel                                            
# 1      Hotel/Restaurant/Cafe  10.0   8.0  22.0  11.0   8.0
#        Retail                  1.0  14.0   0.0   2.0   1.0
# 2      Hotel/Restaurant/Cafe   6.0   0.0   9.0   9.0   4.0
#        Retail                  2.0  15.0   0.0   1.0   1.0
# 3      Hotel/Restaurant/Cafe  36.0  22.0  75.0  45.0  33.0
#        Retail                 23.0  75.0   4.0   1.0   2.0