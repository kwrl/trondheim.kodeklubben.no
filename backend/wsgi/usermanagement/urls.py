from django.conf.urls import patterns, include, url
from .views import login_view

urlpatterns = patterns('',
        url(r'^login/$', login_view, name="login_post"),
)
