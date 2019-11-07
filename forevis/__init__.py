__version__ = '0.1.0'

import matplotlib.pyplot as plt
import mpl_finance
from sys import argv
from Classes.Stoncks import Stoncks
from Classes.Help import call_for_help, inform_query
from Classes.Controller import Controller
from matplotlib.widgets import Button, TextBox

arguments = argv[1:]
if len(arguments) > 0 and (arguments[0] == '-help' or arguments[0] == '-h'):
    call_for_help()

controller = Controller('BTC', 'USD', 1000)

for index, argument in enumerate(arguments):
    if argument == '-from':
        controller.crypto = arguments[index + 1]
    if argument == '-to':
        controller.currency = arguments[index + 1]
    if argument == '-days':
        controller.days = arguments[index + 1]

inform_query(controller.crypto, controller.currency, controller.days)

figure, axe = plt.subplots(figsize = (10,5))

def fetch_info(event=None):
    axe.clear()
    request = Stoncks(function="DIGITAL_CURRENCY_DAILY", crypto=controller.crypto, base_currency=controller.currency)
    response = request.send()
    
    quotes = [
        tuple(
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

    quotes = quotes[::-1]
    quotes = quotes[-int(controller.days):]
    mpl_finance.candlestick_ohlc(axe, quotes, colordown='r', colorup='g')
    axe.xaxis_date()


axprev = plt.axes([0.110, 0.905, 0.1, 0.075])
axnext = plt.axes([0.315, 0.905, 0.1, 0.075])
axsubmit = plt.axes([0.515, 0.905, 0.1, 0.075])
crypto_input = TextBox(axprev, "Crypto", initial=f"{controller.crypto}")
crypto_input.on_text_change(controller.set_crypto)
real_input = TextBox(axnext, "Real", initial=f"{controller.currency}")
real_input.on_text_change(controller.set_currency)
submit = Button(axsubmit, "Pesquisar")
submit.on_clicked(fetch_info)
plt.show()