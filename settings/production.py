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
         'NAME': 'cgx',
         'USER': '',
         'PASSWORD': '',
         'HOST': 'localhost',
         'PORT': '3306',
         'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES';  \
                            SET foreign_key_checks = 0",
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


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = environ.get('EMAIL_HOST', 'in-v3.mailjet.com')
# EMAIL_HOST = 'localhost'
EMAIL_HOST = env.str('EMAIL_HOST', default='localhost')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default='')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default='')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = environ.get('EMAIL_PORT', 587)
# EMAIL_PORT = 1025
EMAIL_PORT = env.int('EMAIL_PORT', default=1025)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
# EMAIL_USE_TLS = False
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=False)

# Email's "from" field
# EMAIL_SENDER = 'TEST <support@dynameyes.com>'
EMAIL_SENDER = env.str('EMAIL_SENDER', default='TEST <support@tgx.com>')  # change to correct value

# Email receiver when EMAIL_TO_TEST is True
EMAIL_TEST_RECEIVER = 'support@tgx.com'  # change to correct value

# When set to true, all emails will be sent to EMAIL_TEST_RECEIVER instead of the user's email
EMAIL_TO_TEST = False

EMAIL_ENABLED = True

# SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION
