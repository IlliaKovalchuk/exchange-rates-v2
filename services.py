import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return {"error": "Unable to fetch data"}
