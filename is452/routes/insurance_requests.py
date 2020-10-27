from flask import request, jsonify

from is452 import app
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import datetime

import json

client = MongoClient("mongodb+srv://is452_admin:mianbaochaoren@is452-project.n0htb.mongodb.net/insurance?retryWrites=true&w=majority")
collection = client.insurance.insurance_requests

@app.route("/create_insurance_request", methods=['POST'])
def create_insurance_request():
    """
    Structure of incoming json data
    {
        'tncs': 'xxx' (type: str),
        'start_date': 'YYYY-MM-DD' (type: str),
        'end_date': 'YYYY-MM-DD' (type: str),
        'insuring_amount': 1234.56 (type: float),
        'premium_amount': 1234.56 (type: float),
        'requester_wallet_addr': 'xxx' (type: str),
        'insurer_wallet_addr': 'xxx' (type: str),
        'status': 'xxx' (type: str)
    }
    """
    insurance_request_data = request.get_json()

    insurance_request_data['start_date'] = datetime.strptime(insurance_request_data['start_date'], "%Y-%m-%d")
    insurance_request_data['end_date'] = datetime.strptime(insurance_request_data['end_date'], "%Y-%m-%d")
    response = collection.insert_one(insurance_request_data)

    return {
        "status": "Insurance request created",
        "request_id": str(response.inserted_id)
    }

@app.route("/get_all_insurance_requests", methods=['GET'])
def get_all_insurance_requests():
    insurance_requests = collection.find()

    if insurance_requests:
        return {
            "status": "All insurance requests has been retrieved",
            "insurance_requests": insurance_requests
        }
    return {
        "status": "No insurance requests in the system at the moment"
    }

@app.route("/get_insurance_request_by_id/<string:request_id>", methods=['GET'])
def get_insurance_request_by_id(request_id):
    insurance_request = collection.find_one({"_id": ObjectId(request_id)})

    if insurance_request:
        insurance_request["_id"] = str(insurance_request["_id"])

        return {
            "status": "Found request",
            "request_record": insurance_request
        }
    
    return {
        "status": "Request ID does not exist in database"
    }

@app.route("/update_insurance_request/<string:request_id>", methods=['POST'])
def update_insurance_request(request_id):
    update_data = request.get_json()

    # check if request_id is valid
    insurance_request = collection.find_one({"_id": ObjectId(request_id)})

    if insurance_request:
        collection.upate_one(
            {
                "_id": ObjectId(request_id)
            },
            {
                "$set": update_data
            }
        )
        return {
            "status": f"Insurance request ({request_id}) has been updated with the new details"
        }

    return {
        "status": "Update request failed"
    }

@app.route("/delete_insurance_request/<string:request_id>", methods=['POST'])
def delete_insurance_request(request_id):
    # check if request_id is valid
    insurance_request = collection.find_one({"_id": ObjectId(request_id)})

    if insurance_request:
        collection.delete_one({"_id": ObjectId(request_id)})

        return {
            "status": f"Successfully deleted insurance request ({request_id})"
        }
    return {
        "status": f"Failed to delete insurance request ({request_id})"
    }