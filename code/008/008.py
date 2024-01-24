from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, round, col, lit

spark = SparkSession.builder.getOrCreate()

usage_hourly = spark.read.csv("data/usage.csv", header=True, inferSchema=True)
weather = spark.read.csv("data/weather.csv", header=True, inferSchema=True)

kwh = round(sum("kwh"), 2).alias("kwh")
cdd = round(col("avg") - lit(65), 2).alias("cdd")

usage = usage_hourly.groupby("date").agg(kwh)
df = usage.join(weather.select("date", cdd), "date")
df.show(5)
# +----------+-------+----+
# |      date|    kwh| cdd|
# +----------+-------+----+
# |2022-07-31|1590.48| 9.3|
# |2022-07-27|2103.65|11.8|
# |2022-06-18|1509.83| 1.4|
# |2022-06-22|2379.26|20.8|
# |2022-06-06|2074.39| 7.8|
# |2022-07-07|1954.09| 8.1|
# |2022-07-05|2112.66|12.1|
# |2022-06-02|2028.83| 9.4|
# |2022-06-05|1777.03| 3.1|
# |2022-07-15|2162.18|12.8|
