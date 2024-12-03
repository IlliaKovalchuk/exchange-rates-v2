from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from services.exchange_rates import get_exchange_rates
from services.currency_converter import convert_currency

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    data = await get_exchange_rates()
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/convert")
async def convert(
    amount: float = Query(..., description="Сума для конвертації"),
    from_currency: str = Query(..., description="Вхідна валюта"),
    to_currency: str = Query(..., description="Вихідна валюта"),
):
    rates = await get_exchange_rates()
    if "error" in rates:
        return rates
    try:
        result = convert_currency(amount, from_currency, to_currency, rates)
        return {"amount": amount, "from": from_currency, "to": to_currency, "converted": result}
    except KeyError:
        return {"error": f"Currency {from_currency} or {to_currency} not found in exchange rates."}

