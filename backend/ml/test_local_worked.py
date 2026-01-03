from decision_engine import get_risk_level, decide

txn = {
    "user_id": "u1",
    "amount": 1200,
    "hour": 2,
    "txn_count_last_24h": 12,
    "location_mismatch": 1,
    "device_familiarity": 0
}

risk = get_risk_level(txn)
final = decide(risk, visa_status="INVALID")

print(risk, final)
