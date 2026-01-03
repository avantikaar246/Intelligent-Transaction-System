# app.py

from flask import Flask, request, jsonify

from ml.feature_utils import extract_features
from decision_engine import decide, map_probability_to_risk
from visa.pav import validate_account
from visa.account_attributes import get_account_attributes
from visa.bin_lookup import get_bin_info

import joblib

app = Flask(__name__)

# Load ML model (trained by Member 1)
model = joblib.load("ml/risk_model.pkl")


@app.route("/evaluate-transaction", methods=["POST"])
def evaluate_transaction():
    data = request.json

    # 1️⃣ Extract ML features
    features = extract_features(data)
    probability = model.predict_proba([features])[0][1]

    # 2️⃣ Convert probability to risk
    risk_level = map_probability_to_risk(probability)

    visa_results = {}

    # 3️⃣ Conditional Visa API calls
    if risk_level in ["MEDIUM", "HIGH"]:
        pav_status = validate_account(data["card_number"])
        visa_results["pav_status"] = pav_status

    if risk_level == "HIGH":
        visa_results["account_attributes"] = get_account_attributes(
            data["card_number"]
        )
        visa_results["bin_info"] = get_bin_info(data["card_bin"])

    # 4️⃣ Final decision
    decision = decide(
        risk_level,
        visa_results.get("pav_status")
    )

    return jsonify({
        "risk_level": risk_level,
        "decision": decision,
        "visa_checks": visa_results
    })


if __name__ == "__main__":
    app.run(debug=True)
