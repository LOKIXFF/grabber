# index.py
from flask import Flask, request, jsonify
import requests
import json
import os

# Initialize the Flask app
app = Flask(__name__)

# --- Flask Routes ---
# os.environ.get("DISCORD_WEBHOOK_URL")
@app.route("/send", methods=["POST"])
def send_message():
    # Retrieve the webhook URL from Vercel's environment variables
    WEBHOOK_URL = "https://discord.com/api/webhooks/1410266517827747942/Jp2PJaqjAi4pxNoJZSOzwGRjVXh2tIKNQzGfA2Qv-OefLEesq_EYsUzLF0o2qviUNPB_"

    if not WEBHOOK_URL:
        return jsonify({"status": "error", "message": "DISCORD_WEBHOOK_URL environment variable is not set."}), 500

    try:
        data = request.json

        payload = {}
        if "content" in data:
            payload["content"] = data["content"]
        if "embeds" in data:
            payload["embeds"] = data["embeds"]

        headers = {"Content-Type": "application/json"}

        r = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(payload))

        if r.status_code == 204:
            return jsonify({"status": "success", "message": "Message sent to Discord"}), 200
        else:
            return jsonify({
                "status": "error",
                "code": r.status_code,
                "response": r.text
            }), 500

    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)}), 500
