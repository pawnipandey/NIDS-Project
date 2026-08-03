from flask import Flask,render_template,session
from routes.auth import auth
from routes.dashboard import dashboard
from routes.monitor import monitor


app = Flask(__name__)
app.secret_key="nids_secret_key"

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(monitor)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/loginpage")
def login_page():
    return render_template("login.html")

@app.route("/registerpage")
def register_page():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)