import sqlite3
from datetime import datetime

def save_log_to_db(log_data):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            process TEXT,
            pid INTEGER,
            user TEXT,
            timestamp TEXT
        )
    ''')
    c.execute('''
        INSERT INTO logs (process, pid, user, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (log_data['process'], log_data['pid'], log_data['user'], log_data['timestamp']))
    conn.commit()
    conn.close()

log_data = {
    "process": "example.exe",
    "pid": 1234,
    "user": "user",
    "timestamp": str(datetime.now())
}
save_log_to_db(log_data)
