from .Stoncks import Stoncks
from random import random

class Graphic:
    def __init__(self, crypto, exchange, analysis):
        self.crypto = crypto
        self.exchange = exchange
        self.analysis = analysis

    def get_data(self):
        request = Stoncks(function="DIGITAL_CURRENCY_DAILY", crypto=self.crypto, base_currency=self.exchange, analysis=self.analysis)
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
        buy = []
        sell = []

        for index, value in enumerate(response["close"]):
            if index >= 5:
                media5.append(sum(response["close"][index-5:index]) / 5)
            else:
                media5.append(response["close"][index] + (random() * response["close"][index] * 0.025))
            if index >= 10:
                media10.append(sum(response["close"][index-10:index]) / 10)
            else:
                media10.append(response["close"][index] + (random() * response["close"][index] * 0.025))
            if index >= 20:
                media20.append(sum(response["close"][index-20:index]) / 20)
            else:
                media20.append(response["close"][index] + (random() * response["close"][index] * 0.025))

            if media5[index - 1] < media10[index - 1] and media5[index] >= media10[index]:
                buy.append(1)
                sell.append(0)
            elif media5[index -  1] > media10[index - 1] and media5[index] <= media10[index]:
                sell.append(1)
                buy.append(0)
            else:
                buy.append(0)
                sell.append(0)

        volume = [response["volume"][x] for x in range(len(response["datetime"]))]
        market = [response["market_cap"][x] for x in range(len(response["datetime"]))]
        time = response["datetime"]
        return quotes, volume, time, market, media5, media10, media20, buy, sell