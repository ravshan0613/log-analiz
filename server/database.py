# server/database.py

import json
from datetime import datetime


def save_log(data):
    # Logga vaqt qo'shish
    data['timestamp'] = str(datetime.now())

    # logs.json fayliga logni yozish
    with open("logs.json", "a") as f:
        f.write(json.dumps(data) + "\n")
