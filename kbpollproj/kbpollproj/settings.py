"""
Django settings for kbpollproj project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(1)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (PROJECT_DIR.child("assets"), )
# pre Django 1.8
TEMPLATE_DIRS = (PROJECT_DIR.child("templates"), )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gw)&^!a+#t3pu66#0mv--%z60%yztb9$8kjl^^^(b*7ulovudp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django_extensions',
)

# add the following lines
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


ROOT_URLCONF = 'kbpollproj.urls'

# following option works in Django 1.8+ only
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # added following lines
                'allauth.account.context_processors.account',
                'allauth.socialaccount.context_processors.socialaccount',
            ],
        },
    },
]

# add the following lines only in Django pre-1.8
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.template.context_processors.debug',
#     'django.template.context_processors.request',
#     'django.contrib.auth.context_processors.auth',
#     'django.contrib.messages.context_processors.messages',
#     'allauth.account.context_processors.account',
#     'allauth.socialaccount.context_processors.socialaccount',
# )

SITE_ID = 1
# to prevent sending out email for confirming user email
# change to "optional" or "mandatory" if you need it
# but you have to find out how to configure email settings
ACCOUNT_EMAIL_VERIFICATION = "none"


WSGI_APPLICATION = 'kbpollproj.wsgi.application'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Set the proper bootstrap classes for the message types we want to use
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.SUCCESS: 'alert-success',
    message_constants.ERROR: 'alert-danger',
}

# Which page to send the user after
# successful login
LOGIN_REDIRECT_URL = '/polls/list/'
# and upon successful logout
ACCOUNT_LOGOUT_REDIRECT_URL = '/polls/list/'
# which form to use for additiona registration info
ACCOUNT_SIGNUP_FORM_CLASS = 'polls.forms.UserProfileForm'
