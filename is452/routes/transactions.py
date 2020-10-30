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
    """
    Structure of incoming json data
    {
        'sending_wallet_addr': 'xxx' (type: str),
        'receiving_wallet_addr': 'xxx' (type: str),
        'transfer_amount': 123.45 (type: float)
    }
    """
    transaction_data = request.get_json()

    response = collection.insert_one(transaction_data)

    return {
        'status': "Transaction logged down",
        'transaction_id': str(response.inserted_id)
    }

@app.route("/get_transactions", methods=["GET"])
def get_transactions():
    transactions = collection.find()

    transformed_transactions = []

    for trxn in transactions:
        trxn['date'] = (trxn['_id'].generation_time).strftime("%Y-%m-%d")
        trxn['_id'] = str(trxn['_id'])
        
        transformed_transactions.append(trxn)

    return {
        'transactions': transformed_transactions
    }


@app.route("/get_user_transactions/<string:user_wallet_address>", methods=["GET"])
def get_user_transactions(user_wallet_address):
    paying_transactions = collection.find({"sending_wallet_addr": user_wallet_address})
    transformed_paying_trxns = []

    if paying_transactions:
        for trxn in paying_transactions:
            trxn['date'] = (trxn['_id'].generation_time).strftime("%Y-%m-%d")
            trxn['_id'] = str(trxn['_id'])

            transformed_paying_trxns.append(trxn)

    receiving_transactions = collection.find({"receiving_wallet_addr": user_wallet_address})
    transformed_receiving_trxns = []

    if receiving_transactions:
        for trxn in receiving_transactions:
            trxn['date'] = (trxn['_id'].generation_time).strftime("%Y-%m-%d")
            trxn['_id'] = str(trxn['_id'])
            
            transformed_receiving_trxns.append(trxn)

    return {
        'paying_transactions': transformed_paying_trxns,
        'receiving_transactions': transformed_receiving_trxns
    }