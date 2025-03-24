from kafka import KafkaProducer
import json
import time
import uuid

producer = KafkaProducer(
    bootstrap_servers='ed-kafka:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

log_file = "logs.json"  

def send_logs():
    with open(log_file, "r") as file:
        logs = json.load(file) 
        for log in logs:
            log["id"] = str(uuid.uuid4()) 
            producer.send("test-topic", log) 
            print(f"Sent: {log}")
            time.sleep(5)

send_logs()
