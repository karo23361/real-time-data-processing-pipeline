from kafka import KafkaProducer
import csv
import time

# Tworzymy producenta Kafka
producer = KafkaProducer(bootstrap_servers='kafka:29092')  # używamy 'kafka:29092' w Dockerze

# Otwórz plik CSV
with open('HDFS_2k.log_structured.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)  # Czytamy wiersze jako słowniki
    for row in csv_reader:
        # Tworzymy wiadomość
        message = f"{row['LineId']},{row['Date']},{row['Time']},{row['Pid']},{row['Level']},{row['Component']},{row['Content']}".encode('utf-8')
        
        # Wysyłamy do topicu 'csv_records'
        producer.send('csv_records', message)
        print(f"Sent: {message.decode('utf-8')}")
        
        # Odczekaj 1 sekundę
        time.sleep(1)

# Czekamy, aż wszystkie wiadomości zostaną wysłane
producer.flush()

