from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

EBIRD_API_KEY = "4hg7070f60mt"

@app.route('/')
def home():
    return jsonify({"message": "Bird Migration API is running"})

@app.route('/birds/<region>')
def get_birds_by_region(region):
    headers = {"X-eBirdApiToken": EBIRD_API_KEY}
    url = f"https://api.ebird.org/v2/data/obs/{region}/recent"
    res = requests.get(url, headers=headers)
    return jsonify(res.json())

@app.route('/birds-live')
def get_live_birds():
    lat = request.args.get("lat", default=40.7)
    lng = request.args.get("lng", default=-74.0)
    dist = request.args.get("dist", default=50)

    headers = {"X-eBirdApiToken": EBIRD_API_KEY}
    url = f"https://api.ebird.org/v2/data/obs/geo/recent?lat={lat}&lng={lng}&dist={dist}&maxResults=100&back=2"

    res = requests.get(url, headers=headers)
    return jsonify(res.json())
