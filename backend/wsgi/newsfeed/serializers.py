from django.forms import widgets
from rest_framework import serializers
from .models import NewsItem

class NewsFullSerializer(serializers.Serializer):
    pk      = serializers.Field()
    title   = serializers.CharField()
    intro   = serializers.CharField()
    body    = serializers.CharField(widget=widgets.Textarea, max_length=10000)


    def restore_object(self, attrs, instance=None):
        if not instance:
            return NewsItem(**attrs)

        instance.title = attrs.get('pk', instance.title)
        instance.title = attrs.get('title', instance.title)
        instance.title = attrs.get('intro', instance.title)
        instance.title = attrs.get('body', instance.title)

        return instance

class NewsHeaderSerializer(serializers.Serializer):
    pk      = serializers.Field()
    title   = serializers.CharField()
    intro   = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if not instance:
            return NewsItem(**attrs)
        
        instance.title = attrs.get('pk', instance.title)
        instance.title = attrs.get('title', instance.title)
        instance.title = attrs.get('intro', instance.title)


