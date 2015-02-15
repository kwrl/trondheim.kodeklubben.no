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
    url(r'^ckeditor/',include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls')),
    url(r'^users/',include('usermanagement.urls')),
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name' : 'form_screen.html'},
        name='login'),
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done',
        'template_name' : 'form_screen.html'},
        name='password_reset'),
        (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
        (r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done'}),
        (r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete')
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
