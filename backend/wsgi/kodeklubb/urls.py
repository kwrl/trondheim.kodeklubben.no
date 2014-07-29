from django.conf.urls import patterns, include, url
from newsfeed.views import NewsView
from usermanagement.views import UserView
from courses.views import CourseView
from django.contrib import admin

from rest_framework import viewsets, routers
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'news',NewsView, base_name='news')
router.register(r'courses',CourseView, base_name='courses')
router.register('accounts', UserView)

urlpatterns = patterns('',
   url(r'^', include(router.urls)),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
