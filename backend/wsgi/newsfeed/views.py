from django.http import HttpResponse
from django.core import serializers as ser

from models import NewsItem

def get_news_headers(request):
    newsitems = NewsItem.objects.all()
    data = ser.serialize('json', newsitems, fields=('id','title','time_stamp','intro'))
    return HttpResponse(data)

def get_news(request, news_id):
    newsitem = NewsItem.objects.get(pk=news_id)
    data = ser.serialize('json', [newsitem])
    return HttpResponse(data)
