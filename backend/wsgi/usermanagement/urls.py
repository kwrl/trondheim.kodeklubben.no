from django.conf.urls import patterns, include, url
from .views import login, logout

urlpatterns = patterns('',
        url(r'^login/$', login),
        url(r'^logout/$', logout),
)
