from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split
from pyspark.sql.types import IntegerType, StringType

# Tworzymy SparkSession z wymaganymi bibliotekami
spark = SparkSession.builder \
    .appName("KafkaToPostgres") \
    .master("local[*]") \
    .config("spark.jars.packages", 
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,"
            "org.postgresql:postgresql:42.7.4") \
    .getOrCreate()

# Ustawienia Kafka
kafka_bootstrap_servers = "kafka:29092"
kafka_topic = "csv_records"

# Wczytanie strumienia z Kafki
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "latest") \
    .load()

processed_df = df_raw.selectExpr("CAST(value AS STRING)") \
    .selectExpr(
        "split(value, ',')[1] AS date",
        "split(value, ',')[2] AS time",
        "CAST(split(value, ',')[3] AS INT) AS pid",
        "split(value, ',')[4] AS level",
        "split(value, ',')[5] AS component",
        "split(value, ',')[6] AS content"
    )

# Funkcja do przetwarzania i zapisywania danych do PostgreSQL
def process_batches(df, epoch_id):
    df.write \
        .format("jdbc") \
        .mode("append") \
        .option("url", "jdbc:postgresql://postgres:5432/kafka_db") \
        .option("dbtable", "csv_records") \
        .option("user", "kafka_user") \
        .option("password", "kafka_pass") \
        .option("driver", "org.postgresql.Driver") \
        .save()
    print(f"✅ Batch {epoch_id} zapisany do PostgreSQL.")

# Uruchomienie strumienia i zapis danych do PostgreSQL
query = processed_df.writeStream \
    .foreachBatch(process_batches) \
    .outputMode("append") \
    .option("checkpointLocation", "checkpoint") \
    .start()

# Czekaj na zakończenie strumienia
query.awaitTermination()
