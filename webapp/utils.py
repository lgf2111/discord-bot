from os import getenv
from authlib.jose import jwt, JoseError


def validate_token(token, operation):
    key = getenv("TOKEN")
    try:
        payload = jwt.decode(token, key)
        return payload
    except JoseError:
        pass
