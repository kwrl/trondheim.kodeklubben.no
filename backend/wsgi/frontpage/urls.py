from django.conf.urls import patterns, include, url
from .views import frontpage

urlpatterns = patterns('',
        url(r'^', frontpage, name="home"),
)
