import requests
from datetime import date

class Stoncks:

    base_url = "https://www.alphavantage.co/query?"
    api_key = "API_KEY"

    def __init__(self, function, crypto, base_currency, trade_type):
        self.function = function
        self.crypto = crypto
        self.base_currency = base_currency
        self.trade_type = trade_type

    def send(self):
        response = requests.get(f'{self.base_url}function={self.function}&symbol={self.crypto}&market={self.base_currency}&apikey={self.api_key}')
        response = response.json()

        dates = list(response["Time Series (Digital Currency Daily)"])

        if self.trade_type == 'st':
            dates = dates[0:40]
        dates = dates[::-1]

        metrics = self.get_metrics(response, dates)

        return {
            "datetime": dates,
            "high": metrics['high'][::-1],
            "low": metrics['low'][::-1],
            "open": metrics['open_values'][::-1],
            "close": metrics['close'][::-1],
            "volume": metrics['volume'][::-1],
            "market_cap": metrics['cap'][::-1]
        }

    def get_metrics(self, response, dates):
        metrics = {}
        metrics['high'] = [int(float(response["Time Series (Digital Currency Daily)"][date][f"2a. high ({self.base_currency})"])) for date in dates]
        metrics['low'] = [int(float(response["Time Series (Digital Currency Daily)"][date][f"3a. low ({self.base_currency})"])) for date in dates]
        metrics['close'] = [int(float(response["Time Series (Digital Currency Daily)"][date][f"4a. close ({self.base_currency})"])) for date in dates]
        metrics['open_values'] = [int(float(response["Time Series (Digital Currency Daily)"][date][f"1a. open ({self.base_currency})"])) for date in dates]
        metrics['volume'] = [int(float(response["Time Series (Digital Currency Daily)"][date][f"5. volume"])) for date in dates]
        metrics['cap'] = [int(float(response["Time Series (Digital Currency Daily)"][date][f"6. market cap (USD)"])) for date in dates]

        return metrics