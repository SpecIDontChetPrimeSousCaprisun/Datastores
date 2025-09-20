from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("ROBLOX_API_KEY")
UNIVERSE_ID = os.getenv("UNIVERSE_ID")

@app.route("/datastores")
def list_datastores():
    try:
        print("a")
        url = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/universe-datastores"
        print("b")
        headers = {"x-api-key": API_KEY}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 3000))
    debug_mode = os.environ.get("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)

@app.route("/datastores")
def home():
    return "✅ Roblox Datastore API is running!"
