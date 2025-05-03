import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

object KafkaToCassandra {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("KafkaToCassandra")
      .master("local[*]")
      .config("spark.cassandra.connection.host", "localhost")
      .config("spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0," +
        "com.datastax.spark:spark-cassandra-connector_2.12:3.0.0")
      .getOrCreate()

    val kafkaBootstrapServers = "kafka:29092"
    val kafkaTopic = "csv_records"

    val dfRaw = spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", kafkaBootstrapServers)
      .option("subscribe", kafkaTopic)
      .option("startingOffsets", "latest")
      .load()

    val processedDF = dfRaw.selectExpr("CAST(value AS STRING)")
      .select(
        split($"value", ",")(1).as("date"),
        split($"value", ",")(2).as("time"),
        split($"value", ",")(3).cast("int").as("pid"),
        split($"value", ",")(4).as("level"),
        split($"value", ",")(5).as("component"),
        split($"value", ",")(6).as("content")
      )

    def processBatches(df: org.apache.spark.sql.DataFrame, epochId: Long): Unit = {
      df.write
        .format("org.apache.spark.sql.cassandra")
        .option("checkpointLocation", "checkpoint")
        .option("keyspace", "csv_keyspace")
        .option("table", "csv_records")
        .mode("append")
        .save()

      println(s"✅ Batch $epochId zapisany do Cassandra.")
    }

    val query = processedDF.writeStream
      .foreachBatch(processBatches)
      .outputMode("append")
      .start()

    query.awaitTermination()

    spark.stop()
  }
}