import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

num_logs = 1_000_000
output_file = 'logs_2.csv'
log_levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
components = ['AuthService', 'PaymentProcessor', 'UserService', 'NotificationEngine', 'DataSync']

def generate_log_entry(line_id):
    date_time = fake.date_time_between(start_date='-30d', end_date='now')
    date = date_time.strftime("%Y-%m-%d")
    time = date_time.strftime("%H:%M:%S")
    pid = random.randint(1000, 9999)
    level = random.choice(log_levels)
    component = random.choice(components)
    content = fake.sentence(nb_words=8)
    event_id = random.randint(100000, 999999)
    event_template = f"TEMPLATE_{random.randint(1, 50)}"
    return [line_id, date, time, pid, level, component, content, event_id, event_template]

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['LineId', 'Date', 'Time', 'Pid', 'Level', 'Component', 'Content', 'EventId', 'EventTemplate'])

    for i in range(1, num_logs + 1):
        log = generate_log_entry(i)
        writer.writerow(log)

print(f"✅ Wygenerowano {num_logs} logów do pliku: {output_file}")




