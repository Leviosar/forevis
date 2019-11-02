import requests
import pandas as pd
import matplotlib.dates as mdates
from datetime import date
from config.env import API_KEY

class Stoncks:

    base_url = "https://www.alphavantage.co/query?"
    api_key = API_KEY

    def __init__(self, function, crypto, base_currency):
        self.function = function
        self.crypto = crypto
        self.base_currency = base_currency

    def send(self):
        response = requests.get(f'{self.base_url}function={self.function}&symbol={self.crypto}&market={self.base_currency}&apikey={self.api_key}')
        response = response.json()

        datas = [value for index, value in enumerate(response["Time Series (Digital Currency Daily)"])]
        numeric_datas = [self.format_data(x) for x in datas]
        high = [int(float(response["Time Series (Digital Currency Daily)"][data][f"2a. high ({self.base_currency})"])) for data in datas]
        low = [int(float(response["Time Series (Digital Currency Daily)"][data][f"3a. low ({self.base_currency})"])) for data in datas]
        close = [int(float(response["Time Series (Digital Currency Daily)"][data][f"4a. close ({self.base_currency})"])) for data in datas]
        open_values = [int(float(response["Time Series (Digital Currency Daily)"][data][f"1a. open ({self.base_currency})"])) for data in datas]
        volume = [int(float(response["Time Series (Digital Currency Daily)"][data][f"5. volume"])) for data in datas]
        cap = [int(float(response["Time Series (Digital Currency Daily)"][data][f"6. market cap (USD)"])) for data in datas]

        return {
            "time": [mdates.date2num(d) for d in numeric_datas],
            "datetime": datas,
            "high": high,
            "low": low,
            "open": open_values,
            "close": close,
            "volume": volume,
            "market_cap": cap
        }

    def format_data(self, data):
        return date(int(data[:4]), int(data[5:7]), int(data[8:]))