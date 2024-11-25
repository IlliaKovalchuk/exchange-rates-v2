import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error_info:
        return {"error": str(error_info)}

def convert_currency(amount: float, from_currency: str, to_currency: str, rates: dict):
    try:
        from_rate = rates["rates"].get(from_currency)
        to_rate = rates["rates"].get(to_currency)

        if not from_rate or not to_rate:
            return {"error": "Currency not found: {from_currency} or {to_currency}"}

        rate = to_rate / from_rate
        converted_amount = amount * rate

        return {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "converted_amount": round(converted_amount, 2),
        }
    except KeyError:
        return {"error": "Invalid rates data"}
