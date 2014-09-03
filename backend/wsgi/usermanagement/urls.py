from django.conf.urls import patterns, include, url
from .views import login_view, EditUserView

urlpatterns = patterns('',
        url(r'^login/$', login_view, name="login_post"),
        url(r'^edit_user/$', EditUserView.as_view(), name='edit_user')
)
