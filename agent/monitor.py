import psutil
import time
import requests

SERVER_URL = "http://localhost:5000/log"

def send_log(data):
    try:
        requests.post(SERVER_URL, json=data)
    except:
        print("Serverga ulanishda xatolik!")

def monitor_processes():
    old_pids = set(psutil.pids())
    while True:
        time.sleep(3)
        new_pids = set(psutil.pids())
        diff = new_pids - old_pids
        for pid in diff:
            try:
                proc = psutil.Process(pid)
                log = {
                    "process": proc.name(),
                    "pid": pid,
                    "user": proc.username()
                }
                print(f"[+] Yangi process: {log}")
                send_log(log)
            except:
                continue
        old_pids = new_pids

if __name__ == "__main__":
    monitor_processes()
