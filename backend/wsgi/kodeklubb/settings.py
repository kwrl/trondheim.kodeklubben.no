"""
Django settings for kodeklubb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
GRAPPELLI_SWITCH_USER=True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n!!2rf9=y1k)eyo*^-657oc%ioh_@1@brpi4s&8i=uw6@@l76g'

DEBUG = True
SITE_ID = 1

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
    BASE_DIR + '/kodeklubb/templates/'
)

ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp@test.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'test@test.com'
EMAIL_HOST_PASSWORD = 'test'
EMAIL_USE_TLS = True

INSTALLED_APPS = (
    'ckeditor',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'newsfeed',
    'courses',
    'filebrowser',
    'bootstrapform',
    'registration',
    'frontpage',
    'usermanagement',
    'class_based_auth_views',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'kodeklubb.urls'

WSGI_APPLICATION = 'kodeklubb.wsgi.application'

#URLS
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"
MEDIA_ROOT = "media"
MEDIA_URL = '/media/'
PRIVATE_MEDIA_ROOT = os.path.join(BASE_DIR, 'private')
PRIVATE_MEDIA_URL = os.path.join(BASE_DIR, 'private')
STATIC_URL= '/static/'
STATIC_ROOT = (os.path.join(BASE_DIR, "static"))
ADMIN_MEDIA_ROOR=MEDIA_ROOT
CKEDITOR_UPLOAD_PATH=MEDIA_ROOT
CKEDITOR_JQUERY_URL='//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {'toolbar': 'Full'}
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


LANGUAGES = [
    ('en-us','English')
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
