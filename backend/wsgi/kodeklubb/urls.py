from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import viewsets, routers

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
    url(r'^$', include('frontpage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'tinymce/', include('tinymce.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^users/',include('usermanagement.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
