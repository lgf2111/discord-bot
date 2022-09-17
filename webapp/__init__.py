from flask import Flask
from waitress import serve
from threading import Thread


app = Flask(__name__)


from webapp import routes


def run():
    serve(app, host="0.0.0.0", port=8080)


def thread_run():
    t = Thread(target=run)
    t.start()
