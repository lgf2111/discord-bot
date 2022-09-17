from flask import Flask
from waitress import serve
from threading import Thread

app = Flask(__name__)


def run():
    serve(app, host="0.0.0.0", port=8000)


def thread_run():
    t = Thread(target=run)
    t.start()
