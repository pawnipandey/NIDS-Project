from flask import Blueprint, request, jsonify,session
from config import get_db_connection

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    data = request.json

    username = data["username"]
    password = data["password"]
    email    = data["email"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password,email) VALUES (%s, %s,%s)",
        (username, password,email)
    )

    conn.commit()

    return jsonify({"message": "User registered successfully"})
@auth.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data["username"]
    password = data["password"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid username or password"})
@auth.route("/logout")
def logout():
    session.clear()
    return "Logout Successfully"