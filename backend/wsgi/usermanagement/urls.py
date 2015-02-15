from django.conf.urls import patterns, include, url
from .views import EditUserView, UserLoginView, UserLogoutView, UserCreateView

urlpatterns = patterns('',
        url(r'^register/$', UserCreateView.as_view(), name="register"),
        #url(r'^login/$', UserLoginView.as_view(), name="login"),
        #url(r'^logout/$', UserLogoutView.as_view(), name="logout"),
        url(r'^edit_user/$', EditUserView.as_view(), name='edit_user')
)
