from replit import db


def init_db():
    keys = ["guilds", "users"]
    for key in keys:
        if not db.get(key):
            db[key] = {}
