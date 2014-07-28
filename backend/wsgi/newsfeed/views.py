from django.http import HttpResponse
from django.core import serializers as ser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import NewsItem
from .serializers import NewsFullSerializer, NewsHeaderSerializer


def api_get_headers(request):
    newsitems = NewsItem.objects.all()
    serializer = NewsHeaderSerializer(newsitems, many=True)
    return Response(serializer.data)

def get_news_headers(request):
    newsitems = NewsItem.objects.all()
    data = ser.serialize('json', newsitems, fields=('id','title','time_stamp','intro'))
    return HttpResponse(data)

def get_news(request, news_id):
    newsitem = NewsItem.objects.get(pk=news_id)
    data = ser.serialize('json', [newsitem])
    return HttpResponse(data)
