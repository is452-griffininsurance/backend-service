from flask import request, jsonify

from is452 import app
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime

import json

client = MongoClient("mongodb+srv://is452_admin:mianbaochaoren@is452-project.n0htb.mongodb.net/insurance?retryWrites=true&w=majority")
collection = client.insurance.transactions

@app.route("/add_transaction", methods=["POST"])
def add_transaction():
    pass

@app.route("/get_transactions", methods=["GET"])
def get_transactions():
    pass

@app.route("/get_user_transactions/<string:user_wallet_address>", methods=["GET"])
def get_user_transactions(user_wallet_address):
    pass