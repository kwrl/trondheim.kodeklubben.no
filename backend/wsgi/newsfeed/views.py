from django.http import HttpResponse
from django.core import serializers as ser
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from models import NewsItem
from .serializers import NewsFullSerializer, NewsHeaderSerializer

class NewsView(viewsets.ViewSet):
    queryset = NewsItem.objects.all().order_by('-time_stamp')

    def list(self,request):
        serializer = NewsHeaderSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        newsitem = get_object_or_404(self.queryset,pk=pk)
        serializer = NewsFullSerializer(newsitem)
        return Response(serializer.data)


