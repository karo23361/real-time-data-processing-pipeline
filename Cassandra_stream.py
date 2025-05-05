from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col


spark = SparkSession.builder \
    .appName("KafkaToCassandra") \
    .master("local[*]") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .getOrCreate()

kafka_bootstrap_servers = "kafka:29092"
kafka_topic = "csv_records"


df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "latest") \
    .load()


processed_df = df_raw.selectExpr("CAST(value AS STRING)") \
    .select(
        split(col("value"), ",")[0].cast("int").alias("lineid"),
        split(col("value"), ",")[1].alias("date"),
        split(col("value"), ",")[2].alias("time"),
        split(col("value"), ",")[3].cast("int").alias("pid"),
        split(col("value"), ",")[4].alias("level"),
        split(col("value"), ",")[5].alias("component"),
        split(col("value"), ",")[6].alias("content")
    )


def write_to_cassandra(batch_df, batch_id):
    batch_df.write \
        .format("org.apache.spark.sql.cassandra") \
        .option("keyspace", "log_data") \
        .option("table", "csv_records") \
        .mode("append") \
        .save()
    print(f"✅ Batch {batch_id} zapisany do Cassandra.")

query = processed_df.writeStream \
    .foreachBatch(write_to_cassandra) \
    .outputMode("append") \
    .option("checkpointLocation", "checkpoint_cas") \
    .start()

query.awaitTermination()
