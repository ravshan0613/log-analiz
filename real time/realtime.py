import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def display_alert(message):
    print(f"[ALERT] {message}")

def check_logs_for_alerts(log_file):
    try:
        with open(log_file, 'r') as f:
            logs = f.readlines()

        for log in logs:
            log_data = json.loads(log)
            if 'error' in log_data.get('process', '').lower():
                message = f"Xatolik topildi: {log_data}"
                display_alert(message)

    except Exception as e:
        print(f"Loglarni tekshirishda xatolik yuz berdi: {e}")

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'C:\\Users\\abdir\\Desktop\\tele\\partfolio\\log\\server\\logs.json':  # Fayl o'zgarganini tekshirish
            print("Log fayli yangilandi!")
            check_logs_for_alerts(event.src_path)

if __name__ == "__main__":
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path='C:\\Users\\abdir\\Desktop\\tele\\partfolio\\log\\server\\', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
