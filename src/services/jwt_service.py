import base64

import jwt
from werkzeug.exceptions import Unauthorized

BEARER_TOKEN_SECRET = "timandjonarethebest"


def jwtValidationAndCreateBearer(basicAuth):
    validUsers = [{"user":"Tim","password":"rox"},{"user":"Jon", "password":"wick"}]
    decodedAuth =  base64.b64decode(basicAuth).decode().split(":")
    decodedAuth[0], decodedAuth[1]
    for validUser in validUsers:
        if(decodedAuth[0] == validUser.get("user")) and decodedAuth[1] == validUser.get("password"):
            return createJwt()

    raise Unauthorized

def createJwt():
    return jwt.encode({}, BEARER_TOKEN_SECRET, algorithm="HS256")

def validateJwtToken(token):
    try:
        bearerToken = token.replace("Bearer ", "")
        jwt.decode(bearerToken, BEARER_TOKEN_SECRET, algorithms="HS256")
    except Exception:
        raise Unauthorized