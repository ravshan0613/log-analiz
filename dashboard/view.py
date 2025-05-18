# dashboard/view.py

import os


def show_logs():
    try:
        log_file_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'logs.json')

        with open(log_file_path, "r") as f:
            logs = f.readlines()
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("logs.json fayli topilmadi. Iltimos, agentni ishga tushiring.")


show_logs()
