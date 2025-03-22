import json
import yaml
from flask import Blueprint, jsonify

content_bp = Blueprint("content", __name__)

# Charger les données depuis un fichier JSON
def load_json_data(filename):
    with open(f"app/static_data/{filename}", "r", encoding="utf-8") as file:
        return json.load(file)

# Charger les données depuis un fichier YAML
def load_yaml_data(filename):
    with open(f"app/static_data/{filename}", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# Endpoint pour récupérer les événements
@content_bp.route("/api/events", methods=["GET"])
def get_events():
    data = load_json_data("events.json")
    return jsonify(data)

# Endpoint pour récupérer les actualités
@content_bp.route("/api/news", methods=["GET"])
def get_news():
    data = load_yaml_data("news.yaml")
    return jsonify(data)
