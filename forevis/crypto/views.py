from django.http import HttpResponse
from django.template import loader
from .Classes.Graphic import Graphic
import json

def index(request):
    template = loader.get_template('crypto/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def chart(request):
    crypto = request.GET.get('crypto').upper()
    exchange = request.GET.get('exchange').upper()
    analysis = request.GET.get('analysis')
    stonkinho = Graphic(crypto, exchange, analysis)
    quotes, volume, time, market, media5, media10, media20, buy, sell = stonkinho.get_data()
    template = loader.get_template('crypto/chart.html')

    context = {
        "crypto": crypto,
        "exchange": exchange,
        "quotes": json.dumps(quotes),
        "volume": volume,
        "time": time,
        "market": market,
        "media5": media5,
        "media10": media10,
        "media20": media20,
        "buy": json.dumps(buy),
        "sell": json.dumps(sell),
    }
    return HttpResponse(template.render(context, request))