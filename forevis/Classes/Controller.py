class Controller:
    def __init__(self, crypto, currency, days):
        self.crypto = crypto
        self.currency = currency
        self.days = days
    
    def set_crypto(self, text):
        self.crypto = text

    def set_currency(self, text):
        self.currency = text