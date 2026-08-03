from config import get_db_connection

def add_network_event(source_ip, destination_ip, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO network_events (source_ip, destination_ip, status) VALUES (%s, %s, %s)",
        (source_ip, destination_ip, status)
    )

    conn.commit()
    cursor.close()
    conn.close()
def get_network_events():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM network_events")

    events = cursor.fetchall()

    cursor.close()
    conn.close()

    return events