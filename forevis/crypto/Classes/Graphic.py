from .Stoncks import Stoncks

class Graphic:
    def __init__(self, crypto, exchange):
        self.crypto = crypto
        self.exchange = exchange

    def get_data(self):
        request = Stoncks(function="DIGITAL_CURRENCY_DAILY", crypto=self.crypto, base_currency=self.exchange)
        response = request.send()

        quotes = [
                    [
                        response["datetime"][x],
                        response["open"][x],
                        response["high"][x],
                        response["low"][x],
                        response["close"][x],
                    ]
            for x in range(len(response["datetime"]))
        ]

        media5 = []
        media10 = []
        media20 = []
        analiseMedia5 = []
        analiseMedia10 = []
        analiseMedia20 = []

        for index, value in enumerate(response["close"]):
            analiseMedia5.append(sum(response["close"][index-5:index]) / 5 >= value)
            analiseMedia10.append(sum(response["close"][index-10:index]) / 10 >= value)
            analiseMedia20.append(sum(response["close"][index-20:index]) / 20 >= value)
            media5.append(sum(response["close"][index-5:index]) / 5)
            media10.append(sum(response["close"][index-10:index]) / 10)
            media20.append(sum(response["close"][index-20:index]) / 20)

        volume = [response["volume"][x] for x in range(len(response["datetime"]))]
        market = [response["market_cap"][x] for x in range(len(response["datetime"]))]
        time = response["datetime"]
        return quotes, volume, time, market, media5, media10, media20, analiseMedia5, analiseMedia10, analiseMedia20