__version__ = '0.1.0'

import matplotlib.pyplot as plt
import mpl_finance
from sys import argv
from Classes.Stoncks import Stoncks
from Classes.Help import call_for_help, inform_query

arguments = argv[1:]
if len(arguments) > 0 and (arguments[0] == '-help' or arguments[0] == '-h'):
    call_for_help()

crypto = 'BTC'
base_currency = 'USD'
days = 1000

for index, argument in enumerate(arguments):
    if argument == '-from':
        crypto = arguments[index + 1]
    if argument == '-to':
        base_currency = arguments[index + 1]
    if argument == '-days':
        days = arguments[index + 1]

inform_query(crypto, base_currency, days)

btc = Stoncks(function="DIGITAL_CURRENCY_DAILY", crypto=crypto, base_currency=base_currency)
btc_data = btc.send()

figure, axe = plt.subplots(figsize = (10,5))

quotes = [
    tuple(
            [
                btc_data["time"][x],
                btc_data["open"][x],
                btc_data["high"][x],
                btc_data["low"][x],
                btc_data["close"][x],
            ]
        ) 
    for x in range(len(btc_data["time"]))
]

quotes = quotes[::-1]
mpl_finance.candlestick_ohlc(axe, quotes, colordown='r', colorup='g')
plt.xlabel('Time')
plt.title('Daily Prices and Volumes for Digital Currency')
plt.show()