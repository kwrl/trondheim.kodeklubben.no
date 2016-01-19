from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site as browsersite
from rest_framework import routers

from courses.viewsets import OpenCourseViewSet, RegistrationViewSet 
from usermanagement.viewsets import UserViewSet

admin.autodiscover()

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'courses', OpenCourseViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    url(r'^$', include('frontpage.urls')),
    url(r'^admin/filebrowser/', include(browsersite.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls')),
    url(r'^accounts/',include('usermanagement.urls')),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
