from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from services.exchange_rates import get_exchange_rates, convert_currency

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    data = get_exchange_rates()
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/convert")
async def convert(
    amount: float = Query(..., description="Сума для конвертації"),
    from_currency: str = Query(..., description="Вхідна валюта"),
    to_currency: str = Query(..., description="Вихідна валюта"),
):
    rates = get_exchange_rates()
    if "error" in rates:
        return rates
    return convert_currency(amount, from_currency, to_currency, rates)
