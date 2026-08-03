from flask import Blueprint, render_template
from models.dashboard_model import get_dashboard_data,get_recent_events,get_recent_alerts

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
def home():
    data = get_dashboard_data()
    events_data = get_recent_events()
    alerts_data = get_recent_alerts()

    return render_template(
        "dashboard.html",
        events=data["events"],
        alerts=data["alerts"],
        threats=data["threats"],
        events_list=events_data,
        alerts_list=alerts_data
    )