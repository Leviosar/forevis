from django.http import HttpResponse
from django.template import loader
from .Classes.Graphic import Graphic
import json

def index(request):
    template = loader.get_template('crypto/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def chart(request):
    crypto = request.GET.get('crypto')
    exchange = request.GET.get('exchange')
    stonkinho = Graphic(crypto, exchange)
    quotes, volume, time, market, media5, media10, media20, analiseMedia5, analiseMedia10, analiseMedia20 = stonkinho.get_data()
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
        "analiseMedia5": analiseMedia5,
        "analiseMedia10": analiseMedia10,
        "analiseMedia20": analiseMedia20
    }
    return HttpResponse(template.render(context, request))