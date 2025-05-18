import json
from datetime import datetime

def save_log(data):
    data['timestamp'] = str(datetime.now())
    with open("logs.json", "a") as f:
        f.write(json.dumps(data) + "\n")
