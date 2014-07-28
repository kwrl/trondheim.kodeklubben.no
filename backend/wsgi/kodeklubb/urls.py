from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.contrib import admin

from rest_framework import viewsets, routers
admin.autodiscover()

class UserViewSet(viewsets.ModelViewSet):
    model = User;

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^news/', include('newsfeed.urls')),
   url(r'^user/', include('usermanagement.urls')),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
