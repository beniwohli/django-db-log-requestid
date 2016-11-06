DATABASES = {
    'default': {
        'ENGINE': 'django_db_log_requestid.sqlite3',
        'NAME': 'tests.db',
        'TEST': {
            'NAME': 'tests.db',
        }
    },
}

INSTALLED_APPS = [
    'tests.testapp',
]

ROOT_URLCONF = 'tests.urls'
DEBUG = True
SITE_ID = 1
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES = [
    'django_db_log_requestid.middleware.DatabaseLogRequestIDMiddleware',
]
SECRET_KEY = '123'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

REQUEST_ID_ENABLE_LOGGING = True