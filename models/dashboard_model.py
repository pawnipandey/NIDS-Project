from config import get_db_connection

def get_dashboard_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM network_events")
    events = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts")
    alerts = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts WHERE status='Attack'")
    threats = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "events": events,
        "alerts": alerts,
        "threats": threats
    }
def get_recent_events():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM network_events ORDER BY id DESC LIMIT 10"
    )

    events = cursor.fetchall()

    cursor.close()
    conn.close()

    return events
def get_recent_alerts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 10")

    alerts = cursor.fetchall()

    cursor.close()
    conn.close()

    return alerts