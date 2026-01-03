# visa/account_attributes.py

import requests
from config import ACCOUNT_ATTR_URL, VISA_USER_ID, VISA_PASSWORD, HEADERS, VISA_CERT, VISA_KEY


def get_account_attributes(card_number: str) -> dict:
    payload = {
        "primaryAccountNumber": card_number
    }

    try:
        response = requests.post(
            ACCOUNT_ATTR_URL,
            json=payload,
            headers=HEADERS,
            auth=(VISA_USER_ID, VISA_PASSWORD),
            cert=(VISA_CERT, VISA_KEY) if VISA_CERT else None,
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "issuer": data.get("issuerName", "UNKNOWN"),
                "country": data.get("issuerCountryCode", "UNKNOWN"),
                "account_type": data.get("accountType", "UNKNOWN")
            }

    except Exception as e:
        print("Account attributes fallback:", e)

    # 🔁 Fallback
    return {
        "issuer": "VISA",
        "country": "IN",
        "account_type": "CREDIT"
    }
