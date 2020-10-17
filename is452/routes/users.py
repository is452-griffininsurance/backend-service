import os
import logging
import requests

import boto3
from boto3.dynamodb.conditions import Key

from dotenv import load_dotenv
from flask import request, jsonify
from is452 import app, requires_auth, requires_scope, AuthError, get_token_auth_header

load_dotenv()
logger = logging.getLogger(__name__)

dynamodb = boto3.resource("dynamodb")

@app.route("/users", methods=['GET'])
@requires_auth
def get_users_info():
    token = get_token_auth_header()
    response = requests.get(
        "https://is452.us.auth0.com/userinfo",
        headers={'Authorization': 'Bearer ' + token})
    user_info = response.json()
    email = user_info['email']
    logger.info("{} has attempted to retrieve user info".format(email))

    # combine Identity Provider's userinfo with ours (e.g. full name)

    table = dynamodb.Table("users")
    response = table.query(
        KeyConditionExpression=Key("email").eq(email)
    )
    print(response['Items'][0]['full_name'])
    user_info.update(response['Items'][0])
    print(user_info)
    

    return user_info

@app.route("/users/onboarding", methods=['POST'])
def onboarding():
    # then get data
    data = request.get_json()
    # post data to dynamodb

    table = dynamodb.Table("users")
    response = table.put_item(
       Item={
            'email': data['email'],
            'full_name': data['name']
        }
    )
    logger.info("{} has successfully completed the onboarding process".format(data['email']))
    print(response)
    return response

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
