# ml/feature_utils.py

def extract_features(txn: dict):
    """
    Extract numerical features from the transaction request.
    Order matters — must match the order used during training!
    
    Features used:
    1. amount
    2. hour (0-23)
    3. txn_count_last_24h
    4. location_mismatch (0 or 1)
    5. device_familiarity (0 or 1) → higher = more familiar
    """
    return [
        float(txn["amount"]),
        int(txn["hour"]),
        int(txn["txn_count_last_24h"]),
        int(txn["location_mismatch"]),
        int(txn["device_familiarity"])
    ]