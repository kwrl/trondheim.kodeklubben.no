from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, LoginForm
from class_based_auth_views.views import LoginView, LogoutView

urlpatterns = patterns('',
    url(r'^register/$',
        CreateView.as_view(
            template_name='form_screen.html',
            form_class=RegistrationForm,
            success_url='/'
        ),
        name='register'),
    url(r'^login/$',
        LoginView.as_view(
            template_name='form_screen.html',
            form_class=LoginForm,
            success_url='/',
        ),
        name='login'),
    url(r'^logout/$',
        LogoutView.as_view(
            template_name='form_screen.html',
        ),
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
