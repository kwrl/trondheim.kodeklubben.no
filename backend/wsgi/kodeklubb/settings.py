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

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n!!2rf9=y1k)eyo*^-657oc%ioh_@1@brpi4s&8i=uw6@@l76g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
        BASE_DIR + '/kodeklubb/templates/'
        )

ALLOWED_HOSTS = ['*']

FILE_UPLOAD_HANDLER = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# Application definition

INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'newsfeed',
        'courses',
        'grappelli',
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
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.doc.XViewMiddleware',
        'django.middleware.common.CommonMiddleware',
        )

ROOT_URLCONF = 'kodeklubb.urls'

WSGI_APPLICATION = 'kodeklubb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL= '/static/'

STATIC_ROOT = (os.path.join(BASE_DIR, "static"))


