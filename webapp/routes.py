from flask import jsonify
from webapp import app
from webapp.utils import validate_token


@app.route("/")
def home():
    return ""


@app.route("/config")
def config():
    return ""


@app.route("/config/<token>", methods=["GET", "POST"])
def config_token(token):
    return jsonify(validate_token(token, "CONFIG"))
