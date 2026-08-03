from flask import Blueprint, request, jsonify
from models.network import add_network_event
from detection.detector import detect_threat
from alerts.alert import generate_alert
from models.alert_model import save_alert

monitor = Blueprint("monitor", __name__)

@monitor.route("/monitor", methods=["POST"])
def monitor_event():
    data = request.json

    source_ip = data["source_ip"]
    destination_ip = data["destination_ip"]
    status = data["status"]
    threat = detect_threat(status)
    alert = generate_alert(source_ip,status)
    if threat:
     save_alert(
        source_ip,
        status,
        alert["alert"]
     )

    add_network_event(source_ip, destination_ip, status)

    return jsonify({
        "message": "Network event added successfully",
        "threat_detected":threat,
        "alert":alert
    })
from models.network import get_network_events

@monitor.route("/events", methods=["GET"])
def events():
    data = get_network_events()

    return jsonify(data)
