from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
    url(r'^register/$',
        CreateView.as_view(
            template_name='form_screen.html',
            form_class=UserCreationForm,
            success_url='/'
        ),
        name='register'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name' : 'form_screen.html'},
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done',
        'template_name' : 'form_screen.html'},
        name='password_reset'),
    url(r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done'},
        name='password_reset_done'),
    url(r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_done')
)
