from django.http import HttpResponse
from django.core import serializers as ser
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import NewsItem
from .serializers import NewsFullSerializer, NewsHeaderSerializer

class NewsHeadersFullViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all().order_by('-time_stamp')
    serializer_class = NewsHeaderSerializer

class NewsHeadersViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all().order_by('-time_stamp')[:20]
    serializer_class = NewsHeaderSerializer

'''
def get_news_headers(request):
    newsitems = NewsItem.objects.all()
    data = ser.serialize('json', newsitems, fields=('id','title','time_stamp','intro'))
    return HttpResponse(data)

def get_news(request, news_id):
    newsitem = NewsItem.objects.get(pk=news_id)
    data = ser.serialize('json', [newsitem])
    return HttpResponse(data)
'''
