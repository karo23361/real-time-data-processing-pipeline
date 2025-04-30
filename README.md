# Real-Time Log Processing and Database Comparison Pipeline

This project implements a **real-time data pipeline** for processing and analyzing logs using **Apache Kafka**, **Apache Spark**, and **Docker**. The goal of this project is not only to handle high-throughput log data but also to **compare the performance and suitability of different databases** (PostgreSQL and Cassandra) in various scenarios.

## Key Features:
- **Data Ingestion**: Logs are collected and streamed using **Apache Kafka**.
- **Stream Processing**: **Apache Spark** processes the data in real time, performing transformations and preliminary aggregations.
- **Data Storage**: Data is stored in two different databases — **PostgreSQL** and **Cassandra** — to compare their performance and behavior.

### Database Comparison:
- Test write and read speeds.
- Analyze performance for different query types.
- Evaluate fault tolerance and scalability.

- **Data Analysis**: (Planned) — Additional analysis and visualizations based on test results.

## Technologies:
- **Apache Kafka**
- **Apache Spark**
- **Docker**
- **PostgreSQL**
- **Cassandra**

## Project Goal:
The objective of the project is to demonstrate in which use cases a relational database (**PostgreSQL**) performs better, and when a NoSQL database (**Cassandra**) is more suitable, specifically in the context of real-time log processing.


![image](https://github.com/user-attachments/assets/04809455-1dda-4a0c-97fa-de1d3031ea90)

Streaming into PostgreSQL:
![image](https://github.com/user-attachments/assets/baab1fcd-720c-4809-8681-d24adb2fae56)

CASSANDRA:
![image](https://github.com/user-attachments/assets/0cf7b9a9-7cbb-438e-bc93-a9ecb1cef55d)


