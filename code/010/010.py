import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.getOrCreate()
df = spark.read.parquet("data/energy-usage.parquet")
my_assembler = VectorAssembler(inputCols=["cdd"], outputCol="feature")
features = my_assembler.transform(df)
model = LinearRegression(featuresCol="feature", labelCol="kwh").fit(features)
fit = model.transform(features).toPandas()

plt.scatter(fit.cdd, fit.kwh, color="#CCCCCC", edgecolors="#4682B4")
plt.plot(fit.cdd, fit.prediction, color="blue")
plt.xlabel("Cooling Degrees (>65F)")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Energy Consumption per CDD with Linear Fit")
plt.savefig("scatter.png")
