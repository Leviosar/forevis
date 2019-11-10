import mpl_finance

from Classes.Stoncks import Stoncks

class Graphic:
    def __init__(self, axe, text_box_data):
        self.axe = axe
        self.text_box_data = text_box_data

    def draw_graphic(self, event=None):
        self.axe.clear()

        quotes, volume, time, market = self.get_data()

        self.axe.set_title(self.text_box_data.crypto)
        self.axe.set(xlabel="Date", ylabel=self.text_box_data.currency)

        mpl_finance.candlestick_ohlc(self.axe, quotes, colordown='r', colorup='g')
        self.axe.plot(time, volume)
        self.axe.xaxis_date()

    def get_data(self):
        request = Stoncks(function="DIGITAL_CURRENCY_DAILY", crypto=self.text_box_data.crypto, base_currency=self.text_box_data.currency)
        response = request.send()

        quotes = [
                (
                    [
                        response["time"][x],
                        response["open"][x],
                        response["high"][x],
                        response["low"][x],
                        response["close"][x],
                    ]
                )
            for x in range(len(response["time"]))
        ]

        volume = [response["volume"][x] for x in range(len(response["time"]))]
        market = [response["market_cap"][x] for x in range(len(response["time"]))]
        time = response["time"]
        quotes = quotes[::-1]
        quotes = quotes[-int(self.text_box_data.days):]

        return quotes, volume, time, market