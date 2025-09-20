from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("ROBLOX_API_KEY")
DEFAULT_UNIVERSE_ID = os.getenv("UNIVERSE_ID")

@app.route("/datastores")
def list_datastores():
    UNIVERSE_ID = request.args.get("uid", DEFAULT_UNIVERSE_ID)
    
    if not universe_id:
        return jsonify({"error": "No universe ID provided"}), 400

    print(f"checking https://apis.roblox.com/datastores/v1/universes/{universe_id}/universe-datastores")
    
    url = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/universe-datastores"
    headers = {"x-api-key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            return jsonify({
                "error": f"{e.response.status_code} {e.response.reason}",
                "text": e.response.text
            }), e.response.status_code
        else:
            return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ Roblox Datastore API is running!"
if __name__ == "__main__":
    # Local testing only
    port = int(os.getenv("PORT", 3000))  # default 3000 if not set
    app.run(host="0.0.0.0", port=port, debug=True)
