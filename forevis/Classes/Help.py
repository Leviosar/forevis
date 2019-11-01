import os
from Classes.Colors import OKGREEN, OKBLUE, ENDC, WARNING

def call_for_help():
    os.system('clear')
    print("We're glad you're using this shit project :D\n")
    print(f"{OKGREEN}Usage: -from [CRYPTO_CURRENCY] -to [CURRENCY] -days [INTEGER] {ENDC}\n")
    print(f"Some supported cryptocurrencies are BITCOIN {OKBLUE}(BTC){ENDC}, ETHEREUM {OKBLUE}(ETH){ENDC}, BITCOIN_CASH {OKBLUE}(BCH){ENDC}, LITECOIN {OKBLUE}(LTC){ENDC}, DOGECOIN {OKBLUE}(DOGE){ENDC}, RIPPLE {OKBLUE}(XRP){ENDC} and EOS {OKBLUE}(EOS){ENDC}, if you're looking for the complete list, go to: {OKBLUE}https://www.alphavantage.co/digital_currency_list/{ENDC}\n")
    print(f"Some supported currencies are US DOLAR {OKBLUE}(USD){ENDC}, BRAZILIAN REAL {OKBLUE}(BRL){ENDC}, EURO {OKBLUE}(EUR){ENDC}, CHINESE CHINACOIN {OKBLUE}(CNY){ENDC}, if you're looking for the complete list go to: {OKBLUE}https://www.alphavantage.co/physical_currency_list/{ENDC}")
    exit()

def inform_query(crypto, base_currency, days):
    os.system('clear')
    print(f"We're fetching data for {WARNING}{crypto}{ENDC} prices in {WARNING}{base_currency}{ENDC} on the last {WARNING}{days}{ENDC} days, keep waiting pls")