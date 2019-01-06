# -*- coding: utf-8 -*-
import os
import logging.config

# from utils.proj_vars import (
#     HOSTNAME,
# )

PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_LOG_DIR = os.path.join(PROJ_DIR, 'log')

# PARAMS
LOG_ROOT_DIR = os.getenv('LOG_ROOT_DIR', DEFAULT_LOG_DIR)
# ROLLBAR_TOKEN = os.getenv('ROLLBAR_TOKEN', 'access_token')
# ROLLBAR_ENV = os.getenv('ROLLBAR_ENV', HOSTNAME)
# ROLLBAR_ENABLED = (os.getenv('ROLLBAR_ENABLED', 'FALSE').upper() == 'TRUE')


modules = [
    'root',
    'libs',
    'django',
]

if not os.path.exists(LOG_ROOT_DIR):
    os.makedirs(LOG_ROOT_DIR)

for m in modules:
    path = os.path.join(LOG_ROOT_DIR, m)
    if not os.path.exists(path):
        os.makedirs(path)


# the automatic configuration process is disabled, not logging itself.
LOGGING_CONFIG = None


# manually configures logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(message)s | %(name)s | %(filename)s-%(lineno)s: %(funcName)s',
        },
        'basic': {
            # including module name, used when adding new handlers
            # 'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            'format': '%(asctime)s | %(levelname)s | %(message)s',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        # 'require_rollbar_enabled': {
        #     '()': 'utils.log.RequireRollbarEnabled',
        # },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        # https://github.com/rollbar/pyrollbar/blob/master/rollbar/logger.py
        # 'rollbar': {
        #     'level': 'ERROR',
        #     'filters': ['require_rollbar_enabled'],
        #     'access_token': ROLLBAR_TOKEN,
        #     'environment': ROLLBAR_ENV,
        #     'class': 'rollbar.logger.RollbarHandler',
        # },
        'django_info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'django/info.log'),
            'formatter': 'verbose',
        },
        'django_warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'django/warning.log'),
            'formatter': 'verbose',
        },
        'django_error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'django/error.log'),
            'formatter': 'verbose',
        },
        'root_info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'root/info.log'),
            'formatter': 'verbose',
        },
        'root_warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'root/warning.log'),
            'formatter': 'verbose',
        },
        'root_error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'root/error.log'),
            'formatter': 'verbose',
        },
        'libs_warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'libs/warning.log'),
            'formatter': 'verbose',
        },
        'libs_error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(LOG_ROOT_DIR, 'libs/error.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['console', 'django_info_file', 'django_warning_file', 'django_error_file'],
            'propagate': False,
        },
        'urllib3': {
            'level': 'WARNING',
            'handlers': ['libs_warning_file', 'libs_error_file'],
        },
        'oss2.api': {
            'level': 'WARNING',
            'handlers': ['libs_warning_file', 'libs_error_file'],
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'root_info_file', 'root_warning_file', 'root_error_file'],
    },
}


logging.config.dictConfig(LOGGING)
