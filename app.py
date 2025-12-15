from flask import Flask, request, send_from_directory
import os
import base64
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json["image"]
    image_data = base64.b64decode(data.split(",")[1])

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "wb") as f:
        f.write(image_data)

    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
