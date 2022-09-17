from webapp import app
from authlib.jose import jwt, JoseError


def validate_token(token):
    key = app.secret_key
    try:
        payload = jwt.decode(token, key)
        return payload
    except JoseError:
        return None


def validate_credentials(email, password):
    pass
