# github.com/bryangoodrich/python-exercises
# code/0009/0009.py

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

spark = SparkSession.builder.getOrCreate()
data = spark.read.parquet("data")
df = data.toPandas()
df.kwh.corr(df.cdd)  # 0.815

plt.rc('axes', labelsize=15)
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.figure(figsize=(10, 6))
fmt = StrMethodFormatter('{x:,g}')

plt.scatter(df.cdd, df.kwh, 
    color='#CCCCCC', edgecolors='#4682B4', s=100)
plt.xlabel("Cooling Degrees", labelpad=10, color="#808080")
plt.ylabel("kWh", labelpad=15, color="#808080")
plt.gca().yaxis.set_major_formatter(fmt)
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("scatter.png")
