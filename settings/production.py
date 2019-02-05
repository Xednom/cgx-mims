"""
Production use of settings
"""

import os
from .base import *
from .local import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['.pythonanywhere.com']

AUTH_USER_MODEL = 'users.CustomUser'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'ENGINE': 'django.db.backends.mysql',
         'NAME': env('DATABASE_NAME'),
         'USER': env('DATABASE_USER'),
         'PASSWORD': env('DATABASE_PASSWORD'),
         'HOST': env('DATABASE_HOST'),
         'PORT': env('DATABASE_PORT'),
         'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
         },
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'src'),
)

STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles')
)

MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

ALLOWED_HOSTS = '*'


# SSL/TLS SETTINGS FOR DJANGO
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 1000000
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_USE_SESSIONS = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
