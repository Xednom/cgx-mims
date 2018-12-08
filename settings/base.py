import json
import os
import logging
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# JSON-based secrets module
with open('secrets.json') as cgx_secret_key:
    secrets = json.loads(cgx_secret_key.read())


def get_secret(setting, secrets=secrets):
    ''' Get the secret variable or return explicit exception '''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# Application  definition

LOCAL_APPS = (
    'users',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PART_APPS = (
    'rest_framework',
    'django_filters',
)

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PART_APPS

AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'src')
)

STATIC_ROOT = (
    os.path.join(BASE_DIR, 'static/web')
)

LOGIN_REDIRECT_URL = ''

LOGIN_URL = ''

LOGIN_EXEMPT_URLS = (
    'admin/',
)

# Logging
def levelname_filter(*args):
    class LevelNameFilter(logging.Filter):
        def filter(self, record):
            return record.levelname.lower() in args
    return LevelNameFilter


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'debug_only': {
            '()': levelname_filter('debug'),
        },
        'info_only': {
            '()': levelname_filter('info'),
        },
        'warn_only': {
            '()': levelname_filter('warning'),
        },
        'error_only': {
            '()': levelname_filter('error', 'critical'),
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'sitelog.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'debug_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'debug.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'info': {
            'level': 'INFO',
            'filters': ['info_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'info.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'warning': {
            'level': 'WARNING',
            'filters': ['warn_only'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'warning.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(os.path.join(BASE_DIR, 'error.log')),
            'maxBytes': 0,
            'backupCount': 0,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['warning', 'error', 'default'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'default': {
            'handlers': ['console', 'default', 'debug', 'info'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
