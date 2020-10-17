import logging
import requests
from flask import request, jsonify
from is452 import app, requires_auth, requires_scope, AuthError, get_token_auth_header

logger = logging.getLogger(__name__)

@app.route("/users", methods=['GET'])
@requires_auth
def get_users_info():
    token = get_token_auth_header()
    response = requests.get(
        "https://is452.us.auth0.com/userinfo",
        headers={'Authorization': 'Bearer ' + token})
    user_info = response.json()
    email = user_info['email']
    return user_info

@app.route("/users/onboarding", methods=['POST'])
def onboarding():
    # get bearer token first
    # token = get_token_auth_header()
    # response = requests.get(
    #     "https://is452.us.auth0.com/userinfo",
    #     headers={'Authorization': 'Bearer ' + token})
    # user_info = response.json()
    # email = user_info['email']

    # then get data
    data = request.get_json()
    # post data to dynamodb
    print(data)
    return data

@app.route("/users/scoped", methods=['GET'])
@requires_auth
def get_users_info_scoped():
    if requires_scope("read:messages"):
        response = "Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)
