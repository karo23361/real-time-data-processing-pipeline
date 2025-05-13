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


![image](https://github.com/user-attachments/assets/04809455-1dda-4a0c-97fa-de1d3031ea90)

Streaming into PostgreSQL:
![image](https://github.com/user-attachments/assets/baab1fcd-720c-4809-8681-d24adb2fae56)

CASSANDRA:
![image](https://github.com/user-attachments/assets/0cf7b9a9-7cbb-438e-bc93-a9ecb1cef55d)


# How to Test the Application

1. Navigate to the folder containing the `docker-compose.yml` file in your terminal. If you're using Docker Desktop, run `docker-compose up` to start the containers.
2. Once the containers are up and running, open your browser and go to `localhost:8888` to access Jupyter Lab.
3. Upload the necessary files to the PySpark machine through the Jupyter Lab interface.
4. Modify the code to process your file. The current code is set up for a specific CSV file format with a predefined split pattern. You'll need to adjust the code according to your CSV structure (e.g., changing split indices to match your data).
5. Create the appropriate database/keyspace depending on whether you're using Cassandra or PostgreSQL. For Cassandra, you need to create a keyspace. For PostgreSQL, create the database.
6. Create the required table in the selected database. Ensure that the table schema matches the data structure you're working with.
7. Run the streaming script (`Cassandra_Stream.py` for Cassandra or `PostgreSQL_Stream.py` for PostgreSQL) to start streaming the data.
8. Run the producer script (`Producer.py`) to simulate data ingestion into Kafka, which will be processed by the streaming application.
9. Observe the data being written to the database. You can query the database (Cassandra or PostgreSQL) to verify that the records have been inserted correctly.
