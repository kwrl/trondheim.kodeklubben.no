from django.forms import widgets
from rest_framework import serializers
from .models import NewsItem

#This should be a subclass of the NewsHeaderSerializer but I haven't bothered yet.
class NewsFullSerializer(serializers.Serializer):
    pk      = serializers.Field()
    title   = serializers.CharField()
    intro   = serializers.CharField()
    body    = serializers.CharField(widget=widgets.Textarea, max_length=10000)

    def restore_object(self, attrs, instance=None):
        if not instance:
            return NewsItem(**attrs)

        instance.pk     = attrs.get('pk', instance.pk)
        instance.title  = attrs.get('title', instance.title)
        instance.intro  = attrs.get('intro', instance.intro)
        instance.body   = attrs.get('body', instance.body)

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


