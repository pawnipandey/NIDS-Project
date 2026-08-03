from config import get_db_connection

def save_alert(source_ip, status, message):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO alerts (source_ip, status, alert_message) VALUES (%s, %s, %s)",
        (source_ip, status, message)
    )

    conn.commit()

    cursor.close()
    conn.close()