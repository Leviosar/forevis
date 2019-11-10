import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

from Classes.Graphic import Graphic

class GUI:
    def __init__(self, text_box_data):
        self.text_box_data = text_box_data
        self.plt = plt
        self.figure, self.axe = plt.subplots()

    def build_gui(self):
        graphic = Graphic(self.axe, self.text_box_data)

        crypto_textbox = self.plt.axes([0.110, 0.905, 0.1, 0.075])
        crypto_input = TextBox(crypto_textbox, "Crypto", initial=f"{self.text_box_data.crypto}")
        crypto_input.on_text_change(self.text_box_data.set_crypto)

        currency_textbox = self.plt.axes([0.315, 0.905, 0.1, 0.075])
        real_input = TextBox(currency_textbox, "Real", initial=f"{self.text_box_data.currency}")
        real_input.on_text_change(self.text_box_data.set_currency)

        axsubmit = self.plt.axes([0.515, 0.905, 0.1, 0.075])
        submit = Button(axsubmit, "Pesquisar")
        submit.on_clicked(graphic.draw_graphic)
        
        self.plt.show()