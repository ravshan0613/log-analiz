#  mini loyha

Kompyuterda ishlayotgan jarayonlarni **real vaqt** rejimida kuzatadigan, loglarni **serverga yuboradigan**, ularni **vizual ko‘rsatadigan** va **xavfli harakatlarni aniqlovchi** mini loyha tizimi.

---

##  Loyihaning Modullari

| Modul              | Tavsifi |
|--------------------|--------|
| `agent/monitor.py` | Kompyuterdagi yangi jarayonlarni kuzatadi va loglarni serverga yuboradi. |
| `server/app.py`    | Flask server: loglarni qabul qiladi va saqlaydi. |
| `server/database.py` | Loglarni JSON faylga yoki SQLite bazasiga saqlaydi. |
| `dashboard/view.py` | Loglarni `logs.json` faylidan o'qib terminalga chiqaradi. |
| `alerts/email_alert.py` | Logda xatolik aniqlansa, email yuboradi. |
| `metplotlib/metplotlib.py`   | Loglar asosida grafik (chizma) hosil qiladi. |
| `realtime/real_time.py` | Log fayl o'zgarsa, real vaqt ogohlantirish beradi. |

---

##  Ishlash Printsipi

1.  **Agent**: Yangi processlar doimiy kuzatib boriladi (`monitor.py`).
2.  **Server**: Loglar REST API orqali qabul qilinadi va saqlanadi (`app.py`).
3.  **Dashboard**: `logs.json` fayli orqali loglarni ko‘rsatadi (`view.py`).
4.  **Alerts**: Email orqali ogohlantiradi (`email_alert.py`).
5.  **Visualization**: Xatoliklar sonini chizmada ko‘rsatadi (`metaplotlip.py`).
6.  **Real-Time**: Log fayli o‘zgarganda terminalda ogohlantirish beradi (`real_time.py`).

---

##  start berish

Quyidagi qadamlar bilan dasturni to‘liq ishga tushirishingiz mumkin:

### 1. Kutubxonalarni o‘rnatish
```bash
pip install -r requirements.txt
