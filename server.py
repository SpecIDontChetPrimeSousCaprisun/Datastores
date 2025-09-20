from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("ROBLOX_API_KEY")

@app.route("/datastores")
def list_datastores():
    # get universe id from query parameter, fallback to default env variable
    print("a")
    universe_id = request.args.get("uid", os.getenv("UNIVERSE_ID"))
    
    print("Requested uid:", universe_id)
    
    if not universe_id:
        return jsonify({"error": "No universe ID provided"}), 400

    url = f"https://apis.roblox.com/datastores/v1/universes/{universe_id}/universe-datastores"
    headers = {"x-api-key": API_KEY}
    print("Request URL:", url)
    
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
    print("aaa")
    return "✅ Roblox Datastore API is running!"

if __name__ == "__main__":
    # Local testing only
    print("legit wtf")
    app.run(host="127.0.0.1", port=3000, debug=True)

