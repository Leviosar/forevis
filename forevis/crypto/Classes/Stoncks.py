import requests
import pandas as pd
import matplotlib.dates as mdates
from datetime import date

class Stoncks:

    base_url = "https://www.alphavantage.co/query?"
    api_key = "API_KEY"

    def __init__(self, function, crypto, base_currency):
        self.function = function
        self.crypto = crypto
        self.base_currency = base_currency

    def send(self):
        response = requests.get(f'{self.base_url}function={self.function}&symbol={self.crypto}&market={self.base_currency}&apikey={self.api_key}')
        response = response.json()

        datas = [value for index, value in enumerate(response["Time Series (Digital Currency Daily)"])]

        metrics = self.get_metrics(response, datas)

        return {
            "datetime": datas,
            "high": metrics['high'][::-1],
            "low": metrics['low'][::-1],
            "open": metrics['open_values'][::-1],
            "close": metrics['close'][::-1],
            "volume": metrics['volume'][::-1],
            "market_cap": metrics['cap'][::-1]
        }

    def format_data(self, data):
        return date(int(data[:4]), int(data[5:7]), int(data[8:]))

    def get_metrics(self, response, datas):
        metrics = {}
        metrics['high'] = [int(float(response["Time Series (Digital Currency Daily)"][data][f"2a. high ({self.base_currency})"])) for data in datas]
        metrics['low'] = [int(float(response["Time Series (Digital Currency Daily)"][data][f"3a. low ({self.base_currency})"])) for data in datas]
        metrics['close'] = [int(float(response["Time Series (Digital Currency Daily)"][data][f"4a. close ({self.base_currency})"])) for data in datas]
        metrics['open_values'] = [int(float(response["Time Series (Digital Currency Daily)"][data][f"1a. open ({self.base_currency})"])) for data in datas]
        metrics['volume'] = [int(float(response["Time Series (Digital Currency Daily)"][data][f"5. volume"])) for data in datas]
        metrics['cap'] = [int(float(response["Time Series (Digital Currency Daily)"][data][f"6. market cap (USD)"])) for data in datas]

        return metrics