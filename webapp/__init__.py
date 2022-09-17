from flask import Flask
from waitress import serve
from threading import Thread
from os import getenv


app = Flask(__name__)

app.config["SECRET_KEY"] = getenv("TOKEN")

from webapp import routes


def run():
    serve(app, host="0.0.0.0", port=8080)


def thread_run():
    t = Thread(target=run)
    t.start()
