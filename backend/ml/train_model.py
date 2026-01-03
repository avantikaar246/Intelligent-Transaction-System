# ml/train_model.py
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from feature_utils import extract_features
import os

# For reproducibility
np.random.seed(42)

def generate_synthetic_data(n_samples=5000):
    """
    Generate synthetic transactions.
    Labels: 1 = fraudulent/high risk, 0 = normal/low risk
    """
    data = []
    labels = []
    
    for _ in range(n_samples):
        # Normal transactions
        if np.random.rand() < 0.95:  # 95% normal
            amount = np.random.exponential(50)  # most txns small
            hour_weights = np.array([1]*8 + [2]*10 + [1]*6)
            hour_probs = hour_weights / hour_weights.sum()
            hour = np.random.choice(24, p=hour_probs)# peak daytime
            txn_count = np.random.poisson(3)
            location_mismatch = 0
            device_familiarity = 1
            label = 0  # low risk
        else:  # Fraudulent patterns
            amount = np.random.exponential(300) + 200  # unusually high
            hour = np.random.choice([23, 0, 1, 2, 3, 4])  # late night
            txn_count = np.random.poisson(15)  # burst activity
            location_mismatch = 1
            device_familiarity = 0
            label = 1  # high risk
        
        # Cap extreme values
        amount = min(amount, 5000)
        txn_count = min(txn_count, 50)
        
        txn = {
            "amount": amount,
            "hour": hour,
            "txn_count_last_24h": txn_count,
            "location_mismatch": location_mismatch,
            "device_familiarity": device_familiarity
        }
        data.append(extract_features(txn))
        labels.append(label)
    
    return np.array(data), np.array(labels)

if __name__ == "__main__":
    print("Generating synthetic data...")
    X, y = generate_synthetic_data(10000)
    
    print("Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X, y)
    
    # Save model
    model_path = os.path.join(os.path.dirname(__file__), "risk_model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    
    print(f"Model trained and saved to {model_path}")
    print(f"Feature weights (importance): {dict(zip(['amount', 'hour', 'txn_count', 'loc_mismatch', 'device_fam'], model.coef_[0]))}")