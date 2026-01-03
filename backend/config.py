# config.py

VISA_SANDBOX_BASE_URL = "https://sandbox.api.visa.com"

# Endpoints
PAV_URL = VISA_SANDBOX_BASE_URL + "/pav/v1/cardvalidation"
ACCOUNT_ATTR_URL = VISA_SANDBOX_BASE_URL + "/paai/fundstransferattinq/v5/cardattributes/fundstransferinquiry"
BIN_LOOKUP_URL = VISA_SANDBOX_BASE_URL + "/filedeliveryservice/v1/binFileTransfer"

# Credentials (sandbox)
VISA_USER_ID = "YOUR_USER_ID"
VISA_PASSWORD = "YOUR_PASSWORD"

# mTLS cert paths (if available)
VISA_CERT = None      # e.g. "cert.pem"
VISA_KEY = None       # e.g. "key.pem"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
