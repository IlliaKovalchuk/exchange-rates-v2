import httpx

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

async def get_exchange_rates():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL, timeout=10)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except httpx.RequestError as req_err:
        return {"error": f"Request error: {req_err}"}
    except ValueError:
        return {"error": "Invalid response format"}

