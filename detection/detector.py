def detect_threat(status):
    suspicious_status = [
        "Attack",
        "Suspicious",
        "Blocked"
    ]

    if status in suspicious_status:
        return True
    else:
        return False