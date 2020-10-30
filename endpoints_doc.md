# Documentation for Insurance Offchain and Transactions APIs

## Insurance Offchain API
### Available Endpoints
1. **POST** `/create_insurance`
- **Input JSON**
```
{
    "contract_address": "0xasdaw1231232",
    "flight_no": "SQ565",
    "flight_date": "2020-12-23",
    "coverage_amount": 1234.56,
    "premium_amount": 1234.56,
    "insured_wallet_addr": "0xkwkwi120"
}
```
   - **Output JSON**
```
{
    "request_id": "5f9b0603c79b6c43b7319059",
    "status": "Insurance request created"
}
```

2. **GET** `/get_all_insurances`
- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "insurance_requests": [
        {
            "_id": "5f9b02ef07c1008333c9ec27",
            "contract_address": "0x023mc0912mdsq0",
            "coverage_amount": 1234.56,
            "flight_date": "Sat, 12 Dec 2020 00:00:00 GMT",
            "flight_no": "SQ123",
            "insured_wallet_addr": "0xa012312310",
            "premium_amount": 1234.56
        },
        {
            "_id": "5f9b033007c1008333c9ec28",
            "contract_address": "0xasd9123osd923",
            "coverage_amount": 1234.56,
            "flight_date": "Wed, 23 Dec 2020 00:00:00 GMT",
            "flight_no": "SQ345",
            "insured_wallet_addr": "0x1u23jsd89askn",
            "premium_amount": 1234.56
        }
    ],
    "status": "All insurance requests has been retrieved"
}
```
3. **GET** `/get_insurance_by_id/<string: insurance_id>`
- **Input JSON**
```
No input required
```
- **Output JSON**
```
{
    "request_record": {
        "_id": "5f9b02ef07c1008333c9ec27",
        "contract_address": "0x023mc0912mdsq0",
        "coverage_amount": 1234.56,
        "flight_date": "Sat, 12 Dec 2020 00:00:00 GMT",
        "flight_no": "SQ123",
        "insured_wallet_addr": "0xa012312310",
        "premium_amount": 1234.56
    },
    "status": "Found request"
}
```

4. **GET** `/get_insurance_by_user/<string: user_wallet_address>`
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
            "flight_date": "Wed, 23 Dec 2020 00:00:00 GMT",
            "flight_no": "SQ345",
            "insured_wallet_addr": "0x1u23jsd89askn",
            "insurers": [],
            "premium_amount": 1234.56,
            "status": "open"
        },
        {
            "_id": "5f9b05e4c79b6c43b7319058",
            "contract_address": "0xq23sdasda",
            "coverage_amount": 1234.56,
            "flight_date": "Wed, 23 Dec 2020 00:00:00 GMT",
            "flight_no": "SQ565",
            "insured_wallet_addr": "0x1u23jsd89askn",
            "insurers": [],
            "premium_amount": 1234.56,
            "status": "open"
        }
    ],
    "insuring_insurances": [
        {
            "_id": "5f9b02ef07c1008333c9ec27",
            "contract_address": "0x023mc0912mdsq0",
            "coverage_amount": 1234.56,
            "flight_date": "Sat, 12 Dec 2020 00:00:00 GMT",
            "flight_no": "SQ123",
            "insured_wallet_addr": "0xa012312310",
            "insurers": [
                {
                    "insuring_amount": 123,
                    "wallet_addr": "0x1u23jsd89askn"
                }
            ],
            "premium_amount": 1234.56,
            "status": "open"
        },
        {
            "_id": "5f9b0603c79b6c43b7319059",
            "contract_address": "0xasdaw1231232",
            "coverage_amount": 1234.56,
            "flight_date": "Wed, 23 Dec 2020 00:00:00 GMT",
            "flight_no": "SQ565",
            "insured_wallet_addr": "0xkwkwi120",
            "insurers": [
                {
                    "insuring_amount": 123,
                    "wallet_addr": "0x1u23jsd89askn"
                }
            ],
            "premium_amount": 1234.56,
            "status": "open"
        }
    ]
}
```

6. **POST** `/add_insurer/<string: contract_address>`
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

3. **GET** `/get_user_transactions/<string: user_wallet_address>`
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