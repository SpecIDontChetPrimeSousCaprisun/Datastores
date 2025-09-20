from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("ROBLOX_API_KEY")

@app.route("/datastores")
def list_datastores():
    # get universe id from query parameter, fallback to default env variable
    url = f"https://apis.roblox.com/datastores/v1/universes/{universe_id}/universe-datastores"
    headers = {"x-api-key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        # detailed error reporting
        if e.response is not None:
            return jsonify({
                "error": f"{e.response.status_code} {e.response.reason}",
                "text": e.response.text
            }), 500
        else:
            return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ Roblox Datastore API is running!"
