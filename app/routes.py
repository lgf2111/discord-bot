from flask import jsonify
from app import app
from app.utils import validate_token


@app.route("/")
def home():
    return ""


@app.route("/config")
def config():
    return ""


@app.route("/config/<token>", methods=["GET", "POST"])
def config(token):
    return jsonify(validate_token(token, "CONFIG"))
