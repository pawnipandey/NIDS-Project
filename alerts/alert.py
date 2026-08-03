def generate_alert(source_ip, status):
    if status in ["Attack", "Suspicious", "Blocked"]:
        return {
            "alert": "Threat Detected",
            "source_ip": source_ip,
            "status": status
        }

    return {
        "alert": "No Threat"
    }