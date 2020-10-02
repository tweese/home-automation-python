import json

from flask import Flask, request, Response
from flask_cors import CORS

from src.services.gpio_service import updateState
from src.services.jwt_service import jwtValidationAndCreateBearer, validateJwtToken

app = Flask(__name__)
CORS(app)


@app.route('/garageDoor/state', methods=['POST'])
def main():
    bearerToken = request.headers.get("Authorization")
    validateJwtToken(bearerToken)

    body = json.loads(request.data)
    state = body['state']
    return updateState(state)


@app.route('/garageDoor/login', methods=['GET'])
def login():
    basicAuth = request.headers.get("Authorization").replace("Basic ", "")

    bearer = jwtValidationAndCreateBearer(basicAuth).decode()
    return Response(json.dumps({"bearerToken": bearer}), status=200, headers={'Content-Type': 'text/json'})




if __name__ == '__main__':
    app.run(debug=True)