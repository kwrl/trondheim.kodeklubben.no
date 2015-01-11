from django.conf.urls import patterns, url
from .views import FrontpageView

urlpatterns = patterns('',
                       url(r'^', FrontpageView.as_view(), name="home"))
