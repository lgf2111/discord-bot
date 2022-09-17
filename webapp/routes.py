from flask import render_template, abort, redirect, url_for, flash

from webapp import app
from webapp.utils import validate_token
from webapp.forms import ConfigForm

from automation.verification import verify

from replit import db


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/config")
def config():
    return ""


@app.route("/config/<token>", methods=["GET", "POST"])
def config_token(token):
    payload = validate_token(token)
    if payload is None:
        return abort(400)

    id = str(payload["id"])
    operation = payload["operation"]
    if operation != "CONFIG":
        return abort(400)

    form = ConfigForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if not (v := verify(email, password)):
            if v is None:
                return abort(500)
            else:
                flash("Credentials invalid, please try again.", "danger")
                return redirect(url_for("config_token", token=token))
        else:
            users = db["users"]
            user = users.get(id)
            if not user:
                users[id] = {}
                user = users[id]
            user.update({"email": email, "password": password})
            users[id] = user
            db["users"] = users
            flash("Credentials stored successfully.", "success")
            return redirect(url_for("home"))

    return render_template("config-form.html", form=form)
