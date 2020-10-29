from flask import request, jsonify

from is452 import app
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime

import json

client = MongoClient("mongodb+srv://is452_admin:mianbaochaoren@is452-project.n0htb.mongodb.net/insurance?retryWrites=true&w=majority")
collection = client.insurance.insurances

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

    insurance_data['flight_date'] = datetime.strptime(insurance_data['start_date'], "%Y-%m-%d")
    response = collection.insert_one(insurance_data)

    return {
        "status": "Insurance request created",
        "request_id": str(response.inserted_id)
    }

@app.route("/get_all_insurances", methods=['GET'])
def get_all_insurances():
    insurances = collection.find()

    if insurances:
        return {
            "status": "All insurance requests has been retrieved",
            "insurance_requests": insurances
        }
    return {
        "status": "No insurances in the system at the moment"
    }

@app.route("/get_insurance_by_id/<string:id>", methods=['GET'])
def get_insurance_by_id(id):
    insurance = collection.find_one({"_id": ObjectId(id)})

    if insurance:
        insurance["_id"] = str(insurance["_id"])

        return {
            "status": "Found request",
            "request_record": insurance
        }
    
    return {
        "status": "Request ID does not exist in database"
    }

# filter requests by user
@app.route("/get_insurance_by_user/<string:user_wallet_addr>", methods=['GET'])
def get_insurance_by_user(user_wallet_addr):
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

    raw_insured_insurances = collection.find({"insured_wallet_address": user_wallet_addr})
    insured_insurances = []

    if raw_insured_insurances:
        for i in raw_insured_insurances:
            i['_id'] = str(i["_id"])
            insured_insurances.append(i)
    
    raw_insuring_insurances = collection.find({"insurers.wallet_addr" : user_wallet_addr})
    insuring_insurances = []

    if raw_insuring_insurances:
        for i in raw_insuring_insurances:
            i["_id"] = str(i["_id"])
            insuring_insurances.append(i)


    return {
        "insured_insurances": insured_insurances,
        "insuring_insurances": insuring_insurances
    }

@app.route("/add_insurer/<string:contract_address>", methods=["POST"])
def add_insurer(contract_address):
    """
    Structure of incoming data:
    {
        "wallet_addr": "xxx", (type: str)
        "insuring_amount": 123.56 (type: float)
    }
    """
    new_insurer_data = request.get_json()

    collection.findAndModify(
        {
            "contract_address": contract_address
        },
        {
            "$addToSet": new_insurer_data
        }
    )

    return {
        "status": f"New insurer ({new_insurer_data['wallet_addr']}) has been added to insurance ({contract_address})"
    }

# @app.route("/update_insurance/<string:id>", methods=['POST'])
# def update_insurance(id):
#     update_data = request.get_json()

#     # check if request_id is valid
#     insurance = collection.find_one({"_id": ObjectId(id)})

#     if insurance:
#         collection.update_one(
#             {
#                 "_id": ObjectId(id)
#             },
#             {
#                 "$set": update_data
#             }
#         )
#         return {
#             "status": f"Insurance ({id}) has been updated with the new details"
#         }

#     return {
#         "status": "Update request failed"
#     }

# @app.route("/delete_insurance_request/<string:request_id>", methods=['POST'])
# def delete_insurance_request(request_id):
#     # check if request_id is valid
#     insurance_request = collection.find_one({"_id": ObjectId(request_id)})

#     if insurance_request:
#         collection.delete_one({"_id": ObjectId(request_id)})

#         return {
#             "status": f"Successfully deleted insurance request ({request_id})"
#         }
#     return {
#         "status": f"Failed to delete insurance request ({request_id})"
#     }