from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import viewsets, routers

from newsfeed.views import NewsView
from usermanagement.views import UserView
from courses.views import CourseView

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'news',NewsView, base_name='news')
router.register(r'courses',CourseView, base_name='courses')
router.register('accounts', UserView)

urlpatterns = patterns('',
   url(r'^', include(router.urls)),
   url(r'^admin/', include(admin.site.urls)),
   url(r'tinymce/', include('tinymce.urls')),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
