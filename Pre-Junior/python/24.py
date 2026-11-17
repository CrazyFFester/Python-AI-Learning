import os
import sys

import requests

if len(sys.argv) != 2:
    sys.exit("Invalid number of command-line arguments")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin",
        params={"apiKey": os.environ.get("COINCAP_API_KEY", "")}
    )

    response.raise_for_status()

    price_usd = float(response.json()["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Failed to fetch Bitcoin price")

print(f"${price_usd * amount:,.4f}")
