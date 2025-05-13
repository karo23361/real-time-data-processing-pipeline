from kafka import KafkaProducer
import csv
import time

producer = KafkaProducer(bootstrap_servers='kafka:29092')  

# Otwórz plik CSV
with open('HDFS_2k.log_structured.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)  
    for row in csv_reader:
        message = f"{row['LineId']},{row['Date']},{row['Time']},{row['Pid']},{row['Level']},{row['Component']},{row['Content']}".encode('utf-8')
        
        producer.send('csv_records', message)
        print(f"Sent: {message.decode('utf-8')}")
        
        time.sleep(1)

producer.flush()

