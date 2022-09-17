from flask import Flask

# from waitress import serve
from threading import Thread

app = Flask(__name__)


def run():
    # serve(app, host="0.0.0.0", port=8000)
    app.run(host="0.0.0.0", port=8000, debug=True)


def thread_run():
    t = Thread(target=run)
    t.start()
