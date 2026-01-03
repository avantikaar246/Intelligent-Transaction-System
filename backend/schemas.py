# schemas.py

TransactionRequest = {
    "user_id": str,
    "amount": float,
    "hour": int,
    "txn_count_last_24h": int,
    "location_mismatch": int,
    "device_familiarity": int,
    "card_number": str,
    "card_bin": str
}

TransactionResponse = {
    "risk_level": str,
    "decision": str,
    "visa_checks": dict
}
