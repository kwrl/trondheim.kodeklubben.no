from django.conf.urls import patterns, include, url

from .views import list_news 

urlpatterns = patterns('',
        url(r'^news/$', list_news),
)
