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
- **WSL (Windows Subsystem for Linux)**

## Project Goal:
The objective of the project is to demonstrate in which use cases a relational database (**PostgreSQL**) performs better, and when a NoSQL database (**Cassandra**) is more suitable, specifically in the context of real-time log processing.


![image](https://github.com/user-attachments/assets/1eb63e71-f6fb-4767-aea8-26b0decae2d8)

Kafka_producer algorithm in action:
![image](https://github.com/user-attachments/assets/15e273e1-aa3e-4484-bec4-c4a9aa87c442)

Checking stream data directly in Kafka:
![image](https://github.com/user-attachments/assets/d3aee9c3-f4c7-4913-938f-7f6895e489ce)

Console output at spark machine:
![image](https://github.com/user-attachments/assets/bc51e39c-ff00-48d6-af81-70dcb9460bc4)

CASSANDRA:
![image](https://github.com/user-attachments/assets/0cf7b9a9-7cbb-438e-bc93-a9ecb1cef55d)


