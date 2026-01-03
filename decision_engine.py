# decision_engine.py
import pickle
import os

from ml.feature_utils import extract_features
from typing import Optional

# Load the trained model once when module is imported
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml", "risk_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def get_risk_probability(txn: dict) -> float:
    """Return fraud probability (0.0 to 1.0)"""
    features = extract_features(txn)
    prob = model.predict_proba([features])[0][1]  # probability of high risk
    return float(prob)

def get_risk_level(txn: dict) -> str:
    """Bucket probability into LOW / MEDIUM / HIGH"""
    prob = get_risk_probability(txn)
    if prob < 0.3:
        return "LOW"
    elif prob <= 0.7:
        return "MEDIUM"
    else:
        return "HIGH"

def decide(risk_level: str, visa_status: Optional[str] = None) -> str:
    """    Final decision engine.
    
    visa_status (provided by Member 2):
      - None (only for LOW risk)
      - "VALID"              → PAV passed
      - "INVALID"            → PAV failed
      - For HIGH risk, Member 2 can pass more detailed status if needed
    """
    if risk_level == "LOW":
        return "APPROVE"
    
    elif risk_level == "MEDIUM":
        if visa_status == "VALID":
            return "APPROVE"
        else:
            return "FLAG"  # includes INVALID or API error
    
    elif risk_level == "HIGH":
        # More strict: even if PAV valid, we block or flag
        if visa_status == "VALID":
            return "FLAG"  # manual review
        else:
            return "BLOCK"
    
    return "BLOCK"  # fallback

def explain_risk(txn: dict) -> dict:
    """
    Returns risk probability and feature contributions.
    Useful for debugging / demo explanation.
    """
    features = extract_features(txn)
    weights = model.coef_[0]
    feature_names = [
        "amount",
        "hour",
        "txn_count_last_24h",
        "location_mismatch",
        "device_familiarity"
    ]

    contributions = {
        name: float(value * weight)
        for name, value, weight in zip(feature_names, features, weights)
    }

    return {
        "risk_probability": get_risk_probability(txn),
        "feature_contributions": contributions
    }
