from flask import Flask, request, send_from_directory
import cloudinary
import cloudinary.uploader
import os
import base64

app = Flask(__name__)

# Cloudinary config (reads from Render env vars)
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json["image"]
    image_data = base64.b64decode(data.split(",")[1])

    result = cloudinary.uploader.upload(
        image_data,
        folder="image-cap"
    )

    return {
        "status": "success",
        "url": result["secure_url"]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
