import requests
from datetime import datetime

# API Endpoint for XRP price
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Fetch XRP price in USD
try:
    response_crypto = requests.get(COINGECKO_API_URL, params={"ids": "ripple", "vs_currencies": "usd"})
    response_crypto.raise_for_status()
    xrp_data = response_crypto.json()
    xrp_price_usd = xrp_data["ripple"]["usd"]
except Exception as e:
    print("Error fetching XRP price:", e)
    exit()

# Display the result
print(f"\nCurrent XRP Price (as of {datetime.now()}): ${xrp_price_usd}")
