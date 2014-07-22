from django.conf.urls import patterns, include, url

from .views import get_news_headers, get_news

urlpatterns = patterns('',
        url(r'^get_news_headers/$', get_news_headers),
        url(r'^get_news/(?P<news_id>[\d]+)', get_news),
)
