from .Stoncks import Stoncks
from random import random

class Graphic:
    def __init__(self, crypto, exchange, trade_type):
        self.crypto = crypto
        self.exchange = exchange
        self.trade_type = trade_type

    def get_data(self):
        request = Stoncks(function="DIGITAL_CURRENCY_DAILY", crypto=self.crypto, base_currency=self.exchange, trade_type=self.trade_type)
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
            media5.append(sum(response["close"][index-5:index]) / 5)
            media10.append(sum(response["close"][index-10:index]) / 10)
            media20.append(sum(response["close"][index-20:index]) / 20)

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
        
        if self.trade_type == 'lt':
            return quotes[10:], volume[10:], time[10:], market[10:], media5[10:], media10[10:], media20[10:], buy[10:], sell[10:]
        else:
            return quotes[10:40], volume[10:40], time[10:40], market[10:40], media5[10:40], media10[10:40], media20[10:40], buy[10:40], sell[10:40]