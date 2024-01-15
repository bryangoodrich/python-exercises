# spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 consumer.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp, date_format, hour, sum

KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'meters'

spark = SparkSession.builder.appName("meter-reader").getOrCreate()
spark.conf.set("spark.sql.streaming.checkpointLocation", "/tmp/checkpoints")

schema = "device string, interval int, endtime string, kwh double"

raw = (spark
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", KAFKA_BROKER)
    .option("subscribe", KAFKA_TOPIC)
    .option("startingOffsets", "earliest")
    .load())

parsed = (raw
    .selectExpr("CAST(value as STRING) as value")
    .select(from_json(col("value"), schema).alias("data"))
    .selectExpr("data.*"))

min15 = (parsed
    .filter("interval = 15")
    .select("device", "endtime", "kwh"))

min15_stream = (min15
    .writeStream
    .format("kafka")
    .option("kafka.bootstrap.servers", KAFKA_BROKER)
    .option("topic", "meters-15") 
    .start())

# min15_agg = (min15
#     .withColumn("ts", to_timestamp(col("endtime")))
#     .withColumn("hour", hour("ts"))
#     .withColumn("endtime", date_format("ts", "yyyy-MM-dd HH:00:00"))
#     .withWatermark("ts", "1 hour")
#     .groupBy("device", "hour", "endtime")
#     .agg(sum(col("kwh")).alias("kwh"))
#     .select("device", "hour", "endtime", "kwh")
#     .writeStream
#     .outputMode("append")
#     .format("kafka")
#     .option("kafka.bootstrap.servers", KAFKA_BROKER)
#     .option("topic", "meters-60")
#     .start())

hourly = (parsed
    .withColumn("hour", hour(to_timestamp(col("endtime"))))
    .select("device", "hour", "endtime", "kwh")
    .writeStream
    .format("kafka").option("kafka.bootstrap.servers", KAFKA_BROKER)
    .option("topic", "meters-60")
    .start())

spark.streams.awaitAnyTermination()
