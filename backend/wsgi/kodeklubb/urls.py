from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

from filebrowser.sites import site as browsersite

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('frontpage.urls')),
    url(r'^admin/filebrowser/', include(browsersite.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'tinymce/', include('tinymce.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^users/',include('usermanagement.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
