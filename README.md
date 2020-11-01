# backend-service

Python Flask backend

## Boilerplate

This repository contains boilerplate codes to build an API service using Python Flask.


## Step by step

A sample endpoint for Calculate Square is in this repo, where you can `POST` to the API endpoint `/square`.

- Go to `square.py` under `app/routes` folder in this template and you will find a post method with name  `/square`
- Write your implementation in this method. This method will be the entry point when you submit your solution for evaluation
- Note the __init__.py file in each folder. This file makes Python treat directories containing it to be loaded in a module

## To run

You will first need to have Python's `virtualenv`. Below are the instructions for Windows.

```sh
pip install virtualenv
```

Next up, create the virtual environment.

```sh
python -m venv venv
```

You can run/activate the virtual environment and install the required packages.

```sh
.\venv\Scripts\activate
pip install -r requirements.txt
```

Finally, run the services!

```sh
python app.py
```

# Documentation for Insurance Offchain and Transactions APIs

## Insurance Offchain API
### Available Endpoints
1. **POST** `/create_insurance?insurance_type=xxx`
<br>
*insurance_type = `flight_delay` / `car`*
- **Input JSON**
<br>
For Flight Delay Insurance
```
{
    "contract_address": "0xasdaw1231232",
    "flight_no": "SQ565",
    "flight_date": "2020-12-23",
    "coverage_amount": 1234.56,
    "premium_amount": 1234.56,
    "insured_wallet_addr": "0xkwkwi120",
    "min_insure_amount": 1234.56,
    "max_insure_amount": 1234.56
}
```
<br>

For Car Insurance
```
{
    "contract_address": "0xasdaw1231232",
    "tncs": "xxx",
    "expiry_date": "2020-12-23",
    "coverage_amount": 1234.56,
    "premium_amount": 1234.56,
    "insured_wallet_addr": "0xkwkwi120",
    "min_insure_amount": 1234.56,
    "max_insure_amount": 1234.56
}
```
   - **Output JSON**
```
{
    "insurance_id": "5f9b0603c79b6c43b7319059",
    "status": "Insurance request created"
}
```

2. **GET** `/get_all_insurances?insurance_type=xxx&status=open`
<br>
*insurance_type = `flight_delay` / `car`*

- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "insurances": [
        {
            "_id": "5f9c449a145edb6cada49a3b",
            "contract_address": "0xC13A1F46B58fCe16C3A583DF8E26BbeF1a497aD2",
            "coverage_amount": 0.0,
            "flight_date": "2020-11-30",
            "flight_no": "SQ306",
            "insurance_type": "flight_delay",
            "insured_wallet_addr": "0x476f44118b3334444e2991b8e3450b855471db6d",
            "insurers": [
                {
                    "insuring_amount": 0.0001,
                    "wallet_addr": "0x476f44118b3334444e2991b8e3450b855471db6d"
                }
            ],
            "max_insured_amount": 0.085,
            "min_insured_amount": 0.0085,
            "percent_insured": 0.001176470588235294,
            "premium_amount": 0.0085,
            "status": "open"
        },
        {
            "_id": "5f9d145d034b70485c73d8a2",
            "contract_address": "0xfc4776D6148A416aD6eae3B41A939a308C5A239f",
            "coverage_amount": 0.0,
            "flight_date": "2020-11-30",
            "flight_no": "SQ306",
            "insurance_type": "flight_delay",
            "insured_wallet_addr": "0xfeb87197abd18ddabd28b58b205936dfb4569b17",
            "insurers": [],
            "max_insured_amount": 0.001,
            "min_insured_amount": 0.0001,
            "percent_insured": 0,
            "premium_amount": 0.0001,
            "status": "open"
        }
    ],
    "status": "All insurances has been retrieved"
}
```
3. **GET** `/get_insurance_by_id?insurance_id=xxx`
- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "insurance": {
        "_id": "5f9eef0ee6433fc292eb1a86",
        "contract_address": "0xasdaw1231232",
        "coverage_amount": 1234.56,
        "flight_date": "2020-12-23",
        "flight_no": "SQ565",
        "insurance_type": "flight_delay",
        "insured_wallet_addr": "0xkwkwi120",
        "insurers": [],
        "max_insure_amount": 1234.56,
        "min_insure_amount": 1234.56,
        "percent_insured": 0,
        "premium_amount": 1234.56,
        "status": "open"
    },
    "status": "Found request"
}
```

4. **GET** `/get_insurance_by_user?user_wallet_address=xxxx`
- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "insured_insurances": [
        {
            "_id": "5f9b033007c1008333c9ec28",
            "contract_address": "0xasd9123osd923",
            "coverage_amount": 1234.56,
            "flight_date": "2020-12-23",
            "flight_no": "SQ345",
            "insurance_type": "flight_delay",
            "insured_wallet_addr": "0x1u23jsd89askn",
            "insurers": [],
            "max_insured_amount": 1234.56,
            "min_insured_amount": 1234.56,
            "percent_insured": 0,
            "premium_amount": 1234.56,
            "status": "open"
        },
        {
            "_id": "5f9b05e4c79b6c43b7319058",
            "contract_address": "0xq23sdasda",
            "coverage_amount": 1234.56,
            "flight_date": "2020-12-23",
            "flight_no": "SQ565",
            "insurance_type": "flight_delay",
            "insured_wallet_addr": "0x1u23jsd89askn",
            "insurers": [],
            "max_insured_amount": 1234.56,
            "min_insured_amount": 1234.56,
            "percent_insured": 0,
            "premium_amount": 1234.56,
            "status": "open"
        }
    ],
    "insuring_insurances": [
        {
            "_id": "5f9b02ef07c1008333c9ec27",
            "contract_address": "0x023mc0912mdsq0",
            "coverage_amount": 1234.56,
            "flight_date": "2020-12-12",
            "flight_no": "SQ123",
            "insurance_type": "flight_delay",
            "insured_wallet_addr": "0xa012312310",
            "insurers": [
                {
                    "insuring_amount": 123,
                    "wallet_addr": "0x1u23jsd89askn"
                }
            ],
            "max_insured_amount": 1234.56,
            "min_insured_amount": 1234.56,
            "percent_insured": 0.09963063763608088,
            "premium_amount": 1234.56,
            "status": "open"
        },
        {
            "_id": "5f9b0603c79b6c43b7319059",
            "contract_address": "0xasdaw1231232",
            "coverage_amount": 1234.56,
            "flight_date": "2020-12-23",
            "flight_no": "SQ565",
            "insurance_type": "flight_delay",
            "insured_wallet_addr": "0xkwkwi120",
            "insurers": [
                {
                    "insuring_amount": 123,
                    "wallet_addr": "0x1u23jsd89askn"
                }
            ],
            "max_insured_amount": 1234.56,
            "min_insured_amount": 1234.56,
            "percent_insured": 0.09963063763608088,
            "premium_amount": 1234.56,
            "status": "open"
        }
    ]
}
```

6. **POST** `/add_insurer?contract_address=xxx`
- **Input JSON**
```
{
    "wallet_addr": "0x1u23jsd89askn",
    "insuring_amount": 123 (can be float also)
}
```
- **Output JSON**
```
{
    "status": "New insurer (0x1u23jsd89askn) has been added to insurance (0x023mc0912mdsq0)"
}
```
----
## Transactions API
### Available Endpoints
1. **POST** `/add_transaction`
- **Input JSON**
```
{
    "sending_wallet_addr": "0x123sdasdas",
    "receiving_wallet_addr": "0xopase0qwe2",
    "transfer_amount": 123.45
}
```
- **Output JSON**
```
{
    "status": "Transaction logged down",
    "transaction_id": "5f9b0c332a2a6d4511bd7291"
}
```

2. **GET** `/get_transactions`
- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "transactions": [
        {
            "_id": "5f9b0c0f2a2a6d4511bd728f",
            "receiving_wallet_addr": "0xaqsdqw123s",
            "sending_wallet_addr": "0x123sdasdas",
            "transfer_amount": 123.45
        },
        {
            "_id": "5f9b0c282a2a6d4511bd7290",
            "receiving_wallet_addr": "0x123sdasdas",
            "sending_wallet_addr": "0xde220230202",
            "transfer_amount": 123.45
        },
        {
            "_id": "5f9b0c332a2a6d4511bd7291",
            "receiving_wallet_addr": "0xopase0qwe2",
            "sending_wallet_addr": "0x123sdasdas",
            "transfer_amount": 123.45
        }
    ]
}
```

3. **GET** `/get_user_transactions?user_wallet_address=xxxx`
- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "paying_transactions": [
        {
            "_id": "5f9b0c0f2a2a6d4511bd728f",
            "date": "2020-10-29",
            "receiving_wallet_addr": "0xaqsdqw123s",
            "sending_wallet_addr": "0x123sdasdas",
            "transfer_amount": 123.45
        },
        {
            "_id": "5f9b0c332a2a6d4511bd7291",
            "date": "2020-10-29",
            "receiving_wallet_addr": "0xopase0qwe2",
            "sending_wallet_addr": "0x123sdasdas",
            "transfer_amount": 123.45
        }
    ],
    "receiving_transactions": [
        {
            "_id": "5f9b0c282a2a6d4511bd7290",
            "date": "2020-10-29",
            "receiving_wallet_addr": "0x123sdasdas",
            "sending_wallet_addr": "0xde220230202",
            "transfer_amount": 123.45
        }
    ]
}
```