__version__ = '0.1.0'

from sys import argv

from Classes.Help import call_for_help, inform_query
from Classes.TextBoxData import TextBoxData
from Classes.GUI import GUI

arguments = argv[1:]
if len(arguments) > 0 and (arguments[0] == '-help' or arguments[0] == '-h'):
    call_for_help()

text_box_data = TextBoxData('BTC', 'USD', 1000)

for index, argument in enumerate(arguments):
    if argument == '-from':
        text_box_data.crypto = arguments[index + 1]
    if argument == '-to':
        text_box_data.currency = arguments[index + 1]
    if argument == '-days':
        text_box_data.days = arguments[index + 1]

inform_query(text_box_data.crypto, text_box_data.currency, text_box_data.days)

gui = GUI(text_box_data)
gui.build_gui()