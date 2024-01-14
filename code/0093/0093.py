# pyspark --packages org.apache.hadoop:hadoop-aws:3.3.1, \
#   com.amazonaws:aws-java-sdk-bundle:1.11.901, \
#   org.apache.hadoop:hadoop-common:3.3.1
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "localhost:9000")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "access_key")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "secretpassword")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.bucket.create", "true")

# Import Existing Dataset from day 91
path = "s3a://invoices/invoices.parquet"
df = spark.read.parquet(path)

# Export Dataset into new bucket
columns= ["Name", "Dept", "Salary"]
data = [("James",   "Sales",   3000), 
        ("Michael", "Sales",   4600), 
        ("Robert",  "Finance", 6100)]
df = spark.createDataFrame(data = data, schema = columns)

path = "s3a://mock/madeup"
df.write.mode("overwrite").csv(path, header=True)
