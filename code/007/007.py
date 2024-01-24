from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

schema = "name string, dob string, children int"
df = spark.read.csv("data/mock.data", header=True, schema=schema)
df.printSchema()
# root
#  |-- name: string (nullable = true)
#  |-- dob: string (nullable = true)
#  |-- children: integer (nullable = true)

df = spark.read.csv("data/mock.data", header=True, inferSchema=True)
df.printSchema()
# root
#  |-- name: string (nullable = true)
#  |-- dob: date (nullable = true)
#  |-- children: integer (nullable = true)

df.show()
# +-----+----------+--------+
# | name|       dob|children|
# +-----+----------+--------+
# |Aaron|2001-01-02|       0|
# | Beth|1990-02-03|       2|
# |Chris|1988-03-04|       1|
# |Derek|1979-04-05|       0|
# +-----+----------+--------+
