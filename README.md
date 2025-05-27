# 🔄💾 Real-Time Data Processing and Database Comparison Pipeline

This project implements a **real-time data pipeline** for processing and analyzing data using **Apache Kafka**, **Apache Spark**, and **Docker**. The goal of this project is not only to handle high-throughput data but also to **compare the performance and suitability of different databases** (PostgreSQL and Cassandra) in various scenarios.

## Key Features:
- **Data Ingestion**: Data are collected and streamed using **Apache Kafka**.
- **Stream Processing**: **Apache Spark** processes the data in real time, performing transformations and preliminary aggregations.
- **Data Storage**: Data is stored in two different databases — **PostgreSQL** and **Cassandra** — to compare their performance and behavior.

### Database Comparison: 
- Test write and read speeds. (Cassandra typically performs better in high-throughput writes, while PostgreSQL provides strong consistency and better support for complex read operations.)
- Analyze performance for different query types. (Cassandra is optimized for denormalized data and performs efficiently only when the partition key is specified - otherwise, queries can degrade significantly in speed due to full cluster scans.)
- Evaluate fault tolerance and scalability. (Evaluate high availability by disconnecting a node from the Cassandra cluster and observing system resilience during reads and writes. In PostgreSQL, test how the system responds to primary key conflicts during insert operations to examine its strict consistency model.)

## 🛠️ Technologies

- 📨 **Apache Kafka**
- ⚡ **Apache Spark**
- 🐳 **Docker**
- 🐘 **PostgreSQL**
- 🍃 **Cassandra**


## Project Goal:
The objective of the project is to demonstrate in which use cases a relational database (**PostgreSQL**) performs better, and when a NoSQL database (**Cassandra**) is more suitable, specifically in the context of real-time log processing.

# Container

![image](https://github.com/user-attachments/assets/fae128d7-0c0b-4e0e-b73c-e1229d25cebd)

# How to Test the Application

1. Navigate to the folder containing the `docker-compose.yml` file in your terminal. If you're using Docker Desktop, run `docker-compose up` to start the containers.

![image](https://github.com/user-attachments/assets/51d48300-c1ac-496d-8f0d-0cf401bfab2c)

2. Once the containers are up and running, open your browser and go to `localhost:8888` to access Jupyter Lab.

![image](https://github.com/user-attachments/assets/dec8202c-a5ec-4f96-81ec-e95c1a776945)

3. Upload the necessary files to the PySpark machine through the Jupyter Lab interface.

![image](https://github.com/user-attachments/assets/573f01e0-9757-4bfa-b75d-d49b413dc888)

4. Modify the code to process your file. The current code is set up for a specific CSV file format with a predefined split pattern. You'll need to adjust the code according to your CSV structure (e.g., changing split indices to match your data).

![image](https://github.com/user-attachments/assets/75ecc911-ce73-46e8-b0a3-5620ab62706a)


5. Create the appropriate database/keyspace depending on whether you're using Cassandra or PostgreSQL. For Cassandra, you need to create a keyspace. For PostgreSQL, create the database.

In PostgreSQL container:

PostgreSQL
```sql
Already created from the beggining (kafka_db).

```
In Cassandra container:

Cassandra:
```sql
CREATE KEYSPACE IF NOT EXISTS log_data
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};
```
6. Create the required table in the selected database. Ensure that the table schema matches the data structure you're working with.

In PostgreSQL container:

PostgreSQL
```sql
CREATE TABLE csv_records (
    date TEXT,
    time TEXT,
    pid INT,
    level TEXT,
    component TEXT,
    content TEXT
);
```
In Cassandra container:

Cassandra:
```sql
CREATE TABLE IF NOT EXISTS csv_records (
    lineid INT,
    date TEXT,
    time TEXT,
    pid INT,
    level TEXT,
    component TEXT,
    content TEXT,
    PRIMARY KEY ((date), lineid)
);
```
7. Create a Kafka topic that will be used for streaming the CSV records.

In kafka container:

```bash
kafka-topics --create --topic csv_records --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

kafka-topics --bootstrap-server localhost:9092 --delete --topic csv_records
```

8. Run the streaming script (`Cassandra_Stream.py` for Cassandra or `PostgreSQL_Stream.py` for PostgreSQL) to start streaming the data.

In pyspark-jupter-lab container:

Cassandra:
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0 Cassandra_stream.py
```
PostgreSQL
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0,org.postgresql:postgresql:42.7.4 PostgreSQL_stream.py
```
9. Run the producer script (`Producer.py`) to simulate data ingestion into Kafka, which will be processed by the streaming application.

In pyspark-jupter-lab container:

```bash
python Producer.py
```
10. Observe the data being written to the database. You can query the database (Cassandra or PostgreSQL) to verify that the records have been inserted correctly.

![image](https://github.com/user-attachments/assets/ba8dff7c-0354-46d5-9020-2c2b3a10c9c5)
