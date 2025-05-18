import requests
import json

TOKEN = 'api token'
CHAT_ID = 'user id'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_alert_to_telegram(alert_message):
    payload = {
        'chat_id': CHAT_ID,
        'text': alert_message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Alert Telegramga yuborildi!")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

def check_logs_for_alerts(log_file_path):
    try:
        with open(log_file_path, 'r') as f:
            logs = f.readlines()
            for log in logs:
                if "ERROR" in log or "ALERT" in log:
                    send_alert_to_telegram(log.strip())
    except FileNotFoundError:
        print(f"Log fayli topilmadi. Iltimos, {log_file_path} faylini tekshirib ko'ring.")


if __name__ == "__main__":
    check_logs_for_alerts('server/logs.json')
