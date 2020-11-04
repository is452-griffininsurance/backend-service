from flask import request, jsonify

from is452 import app
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime

import json

client = MongoClient("mongodb+srv://is452_admin:mianbaochaoren@is452-project.n0htb.mongodb.net/insurance?retryWrites=true&w=majority")
collection = client.insurance.insurances

date_elements = {
    "flight_delay": "flight_date",
    "car": "expiry_date"
}

@app.route("/create_insurance", methods=['POST'])
def create_insurance():
    """
    Structure of incoming json data
    {
        'contract_address': 'xxx', (type: str)
        'flight_no': 'xxx' (type: str),
        'flight_date': 'YYYY-MM-DD' (type: str),
        'coverage_amount': 1234.56 (type: float),
        'premium_amount': 1234.56 (type: float),
        'insured_wallet_addr': 'xxxx' (type: str)
    }
    """
    insurance_type = request.args.get("insurance_type", None)
    insurance_data = request.get_json()

    """
    Structure of document to be stored
    {
        'contract_address': 'xxx', (type: str)
        'flight_no': 'xxx' (type: str),
        'flight_date': 'YYYY-MM-DD' (type: datetime),
        'coverage_amount': 1234.56 (type: float),
        'premium_amount': 1234.56 (type: float),
        'insured_wallet_addr': 'xxxx' (type: str),
        'insurers': [] (type: str),
        'status': 'open' (type:str)
    }
    """
    if insurance_type == "flight_delay":
        insurance_data['flight_date'] = datetime.strptime(insurance_data['flight_date'], "%Y-%m-%d")
    else:
        insurance_data['expiry_date'] = datetime.strptime(insurance_data['flight_date'], "%Y-%m-%d")

    insurance_data['insurers'] = []
    insurance_data['status'] = 'open'
    insurance_data['insurance_type'] = insurance_type
    response = collection.insert_one(insurance_data)

    return {
        "status": "Insurance record created",
        "insurance_id": str(response.inserted_id)
    }

@app.route("/get_all_insurances", methods=['GET'])
def get_all_insurances():
    insurance_type = request.args.get("insurance_type", None)
    status = request.args.get("status", None)
    insurances = collection.find({"$and": [{"insurance_type": insurance_type}, {"status": status}]})
    date_element = date_elements[insurance_type]

    transformed_insurances = []

    for i in insurances:
        i['_id'] = str(i['_id'])
        i[date_element] = i[date_element].strftime("%Y-%m-%d")
        cum_insured_amt = 0
        if i["insurers"]:
            for insurer in i["insurers"]:
                cum_insured_amt += float(insurer['insuring_amount'])
        
        if cum_insured_amt > 0:
            i['percent_insured'] = cum_insured_amt/float(i['max_insured_amount'])
        else:
            i['percent_insured'] = cum_insured_amt
        
        transformed_insurances.append(i)

    if insurances:
        return {
            "status": "All insurances has been retrieved",
            "insurances": transformed_insurances
        }
    return {
        "status": "No insurances in the system at the moment"
    }

@app.route("/get_insurance_by_id", methods=['GET'])
def get_insurance_by_id():
    insurance_id = request.args.get("insurance_id", None)
    insurance = collection.find_one({"_id": ObjectId(insurance_id)})
    date_element = date_elements[insurance['insurance_type']]
    if insurance:
        insurance["_id"] = str(insurance["_id"])
        insurance[date_element] = insurance[date_element].strftime("%Y-%m-%d")

        cum_insured_amt = 0
        if insurance["insurers"]:
            for insurer in insurance["insurers"]:
                cum_insured_amt += insurer['insuring_amount']
        
        if cum_insured_amt > 0:
            insurance['percent_insured'] = cum_insured_amt/insurance['max_insured_amount']
        else:
            insurance['percent_insured'] = cum_insured_amt

        return {
            "status": "Found request",
            "insurance": insurance
        }
    
    return {
        "status": "Insurance ID does not exist in database"
    }

# filter requests by user
@app.route("/get_insurance_by_user", methods=['GET'])
def get_insurance_by_user():
    """
    Structure of document to be stored
    {
        'contract_address': 'xxx', (type: str)
        'flight_no': 'xxx' (type: str),
        'flight_date': 'YYYY-MM-DD' (type: datetime),
        'coverage_amount': 1234.56 (type: float),
        'premium_amount': 1234.56 (type: float),
        'insured_wallet_addr': 'xxxx' (type: str),
        'insurers': [
            {"wallet_addr": "xxx" (type: str), "insuring_amount": 123.56 (type: float)},
            {"wallet_addr": "xxx" (type: str), "insuring_amount": 123.56 (type: float)},
            ...
        ] (type: str),
        'status': 'open' (type:str)
    }
    """
    user_wallet_addr = request.args.get("user_wallet_addr", None)
    raw_insured_insurances = collection.find({"insured_wallet_addr": user_wallet_addr})
    insured_insurances = []
    
    if raw_insured_insurances:
        for i in raw_insured_insurances:
            i['_id'] = str(i["_id"])
            i['flight_date'] = i['flight_date'].strftime("%Y-%m-%d")
            cum_insured_amt = 0
            if i["insurers"]:
                for insurer in i["insurers"]:
                    cum_insured_amt += insurer['insuring_amount']
            
            if cum_insured_amt > 0:
                i['percent_insured'] = cum_insured_amt/i['max_insured_amount']
            else:
                i['percent_insured'] = cum_insured_amt

            insured_insurances.append(i)
    
    raw_insuring_insurances = collection.find({"insurers.wallet_addr" : user_wallet_addr})
    insuring_insurances = []

    if raw_insuring_insurances:
        for i in raw_insuring_insurances:
            i["_id"] = str(i["_id"])
            i['flight_date'] = i['flight_date'].strftime("%Y-%m-%d")
            cum_insured_amt = 0
            if i["insurers"]:
                for insurer in i["insurers"]:
                    cum_insured_amt += insurer['insuring_amount']
            
            if cum_insured_amt > 0:
                i['percent_insured'] = cum_insured_amt/i['max_insured_amount']
            else:
                i['percent_insured'] = cum_insured_amt

            insuring_insurances.append(i)


    return {
        "insured_insurances": insured_insurances,
        "insuring_insurances": insuring_insurances
    }

@app.route("/add_insurer", methods=["POST"])
def add_insurer():
    """
    Structure of incoming data:
    {
        "wallet_addr": "xxx", (type: str)
        "insuring_amount": 123.56 (type: float)
    }
    """
    contract_address = request.args.get("contract_address", None)
    new_insurer_data = request.get_json()

    collection.find_one_and_update(
        {
            "contract_address": contract_address
        },
        {
            "$addToSet": {"insurers": new_insurer_data}
        }
    )

    transaction_data = {
        "sending_wallet_addr": new_insurer_data['wallet_addr'],
        "receiving_wallet_addr": contract_address,
        "transfer_amount": new_insurer_data['insuring_amount']
    }
    transaction_collection = client.insurance.transactions

    response = transaction_collection.insert_one(transaction_data)


    return {
        "status": f"New insurer ({new_insurer_data['wallet_addr']}) has been added to insurance ({contract_address})"
    }
