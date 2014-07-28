from django.conf.urls import patterns, include, url
from newsfeed.views import NewsHeadersViewSet, NewsHeadersFullViewSet
from usermanagement.views import UserView
from django.contrib import admin

from rest_framework import viewsets, routers
admin.autodiscover()

router = routers.DefaultRouter()
router.register('news_list',NewsHeadersViewSet)
router.register('news_list_full', NewsHeadersFullViewSet)
router.register('accounts', UserView)

urlpatterns = patterns('',
   url(r'^', include(router.urls)),
   url(r'^admin/', include(admin.site.urls)),
   #url(r'^news/', include('newsfeed.urls')),
   #url(r'^user/', include('usermanagement.urls')),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
