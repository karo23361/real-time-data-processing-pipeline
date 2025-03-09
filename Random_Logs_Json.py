import json
import random
from datetime import datetime

log_levels = ["INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"]

log_messages = {
    "INFO": ["Service started", "User logged in", "Data successfully saved", "Request processed"],
    "ERROR": ["Failed to connect to DB", "File not found", "Out of memory", "Permission denied"],
    "WARNING": ["Slow response time", "Disk space running low", "Deprecation warning", "Invalid input detected"],
    "DEBUG": ["Debugging data received", "Variable value: 42", "Entering function X", "Processing step Y"],
    "CRITICAL": ["System crash", "Unrecoverable error", "Service unavailable", "Data corruption detected"]
}
def generate_log():
    level = random.choice(log_levels)
    message = random.choice(log_messages[level])
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "level": level,
        "message": message,
        "source": "MyApp",  
        "request_id": random.randint(1000, 9999),  
        "user_id": random.randint(1, 100)  
    }
    
    return log_entry

def generate_logs(num_logs=500):
    logs = []
    for _ in range(num_logs):
        logs.append(generate_log())
    return logs


if __name__ == "__main__":
    generated_logs = generate_logs(500)  

file_path = "PATH/logs.json"  

with open(file_path, "w") as f:
    json.dump(generated_logs, f, indent=4)



