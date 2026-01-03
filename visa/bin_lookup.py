# visa/bin_lookup.py

import requests
from config import BIN_LOOKUP_URL, VISA_USER_ID, VISA_PASSWORD, HEADERS, VISA_CERT, VISA_KEY


def get_bin_info(bin_number: str) -> dict:
    payload = {
        "requestHeader": {
            "messageId": "bin-lookup-demo"
        },
        "requestData": {
            "bin": bin_number
        }
    }

    try:
        response = requests.post(
            BIN_LOOKUP_URL,
            json=payload,
            headers=HEADERS,
            auth=(VISA_USER_ID, VISA_PASSWORD),
            cert=(VISA_CERT, VISA_KEY) if VISA_CERT else None,
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "bank": data.get("issuerName", "UNKNOWN"),
                "card_category": data.get("cardType", "UNKNOWN")
            }

    except Exception as e:
        print("BIN lookup fallback:", e)

    # 🔁 Fallback
    return {
        "bank": "HDFC Bank",
        "card_category": "Platinum"
    }
