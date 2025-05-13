CREATE KEYSPACE IF NOT EXISTS log_data
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};


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
