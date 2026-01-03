# app.py

from flask import Flask, request, jsonify

from ml.feature_utils import extract_features
from decision_engine import decide, get_risk_level
from visa.pav import validate_account
from visa.account_attributes import get_account_attributes
from visa.bin_lookup import get_bin_info

from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5174"])

# Temporary in-memory "database"
users = {}  # {username/email: password}

# Signup route
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = password
    print(f"New user signup: {username}")

    return jsonify({"success": True, "message": f"User {username} signed up successfully"}), 200

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if username in users and users[username] == password:
        print(f"User login successful: {username}")
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401


# Transaction evaluation route (your existing code)
@app.route("/evaluate-transaction", methods=["POST"])
def evaluate_transaction():
    data = request.json

    risk_level = get_risk_level(data)
    visa_results = {}

    if risk_level in ["MEDIUM", "HIGH"]:
        pav_status = validate_account(data["card_number"])
        visa_results["pav_status"] = pav_status

    if risk_level == "HIGH":
        visa_results["account_attributes"] = get_account_attributes(data["card_number"])
        visa_results["bin_info"] = get_bin_info(data["card_bin"])

    decision = decide(risk_level, visa_results.get("pav_status"))

    return jsonify({
        "risk_level": risk_level,
        "decision": decision,
        "visa_checks": visa_results
    })


if __name__ == "__main__":
    app.run(debug=True)
