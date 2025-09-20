from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("ROBLOX_API_KEY")
UNIVERSE_ID = os.getenv("UNIVERSE_ID")

@app.route("/datastores")
def list_datastores():
    try:
        url = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/standard-datastores"
        headers = {"x-api-key": API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ Roblox Datastore API is running!"
