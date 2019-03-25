import json
import os
import logging
from django.conf import global_settings
from django.core.exceptions import ImproperlyConfigured
import environ

ROOT_DIR = environ.Path(__file__) - 2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool, False), )  # set default values and casting
env_file = str(ROOT_DIR.path('.env'))
env.read_env(env_file)

# Application  definition

LOCAL_APPS = (
    'carrier',
    'cgx',
    'dme',
    'insurance',
    'paincreamandfootbath',
    'supplies',
    'users',
    'jet.dashboard',
    'jet',
    #'grappelli',
    'web',
    'notification',
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
    'import_export',
    'corsheaders',
    'storages',
    'rangefilter',
)

IMPORT_EXPORT_USE_TRANSACTIONS = True

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PART_APPS

AUTH_USER_MODEL = 'users.CustomUser'

CORS_ORIGIN_ALLOW_ALL = False

CSRF_USE_SESSIONS = True

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000',
)

CORS_ALLOW_HEADERS = (
    'x-csrftoken'
)

# ANYMAIL CONFIGURATION
ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-6e093d8bd184ccb2173875fa2f72ba07",
    "MAILGUN_SENDER_DOMAIN": 'veezzo.cz',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "sender@tgx.com"  # if you don't already have this in settings
# END ANYMAIL CONFIGURATION


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

FILE_UPLOAD_HANDLERS = (
                        "django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler",
                        'django.core.files.uploadhandler.MemoryFileUploadHandler',
                        'django.core.files.uploadhandler.TemporaryFileUploadHandler',
                        )


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'drf_renderer_xlsx.renderers.XLSXRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # commented this one out for Django jet admin theme
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Amazon S3 configs
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'tsg-media'
AWS_AUTO_CREATE_BUCKET = env('AWS_AUTO_CREATE_BUCKET')
AWS_S3_ENCRYPTION = env('AWS_S3_ENCRYPTION')
AWS_S3_FILE_OVERWRITE = env('AWS_S3_FILE_OVERWRITE')
AWS_S3_USE_SSL = env('AWS_S3_USE_SSL')
AWS_DEFAULT_ACL = env('AWS_DEFAULT_ACL')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'media'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'media'),
]
MEDIA_ROOT = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' # Don't use this, we only use static in the project folder
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

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

LOGIN_REDIRECT_URL = ''

LOGIN_URL = '/login/'

LOGIN_EXEMPT_URLS = (
    'admin/',
)

# Grappelli customization(s)
# GRAPPELLI_ADMIN_TITLE = 'TSG Administration'
# GRAPPELLI_AUTOCOMPLETE_LIMIT = 7
# GRAPPELLI_SWITCH_USER = True
# GRAPPELLI_CLEAN_INPUT_TYPES = True

# Django Jet Customization(s)
JET_CHANGE_FORM_SIBLING_LINKS = True
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'

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


LOGIN_URL = 'web:login'

LOGIN_EXEMPT_URLS = (
    'admin/'
    'web:login'
)
