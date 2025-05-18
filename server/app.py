from flask import Flask, request
from database import save_log

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log_data():
    data = request.json
    save_log(data)
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
