from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
spark = SparkSession.builder.appName("FraudDetection").getOrCreate()
df_kafka = spark.readStream.format("kafka") \
 .option("kafka.bootstrap.servers","localhost:9092") \
 .option("subscribe","bank_topic") \
 .load()
schema = StructType([
 StructField("nama", StringType()),
 StructField("rekening", StringType()),
 StructField("jumlah", IntegerType()),
 StructField("lokasi", StringType()),
 StructField("status", StringType())  # ✅ WAJIB
])
df = df_kafka.selectExpr("CAST(value AS STRING)") \
 .select(from_json(col("value"), schema).alias("data")) \
 .select("data.*")
# Masking
df = df.withColumn("rekening_masked",
 concat(lit("****"), col("rekening").substr(-2,2)))
# Encryption
df = df.withColumn("jumlah_encrypted",
 base64(col("jumlah").cast("string")))
query = df.writeStream \
 .format("parquet") \
 .option("path","stream_data/realtime_output/") \
 .option("checkpointLocation","data/checkpoints/") \
 .start()
query.awaitTermination()