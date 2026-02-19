from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Jenkins CI/CD Pipeline + Render 🚀"
