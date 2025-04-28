"""
Enhanced logging configuration for PMS project.
Features:
- Directory auto-creation
- Separate log files for different levels
- Proper rotation and retention
- Structured formatting
- Environment-based configuration
"""

import os
from sys import stdout
from datetime import datetime
from pathlib import Path

# Logging directory setup
BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Create logs directory if it doesn't exist
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR, exist_ok=True)

# Current date for log naming
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

# Environment detection
ENVIRONMENT = os.getenv("DJANGO_ENV", "development").lower()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} | {levelname} | {process:d} | {thread:d} | {module} | {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} | {levelname} | {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG' if ENVIRONMENT == 'development' else 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'stream': stdout,
            'formatter': 'simple',
        },
        'production_console': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, f'debug-{CURRENT_DATE}.log'),
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, f'errors-{CURRENT_DATE}.log'),
            'when': 'midnight',
            'backupCount': 30,
            'formatter': 'verbose',
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, f'info-{CURRENT_DATE}.log'),
            'when': 'midnight',
            'backupCount': 14,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'production_console', 'debug_file', 'error_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['error_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['error_file', 'info_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'Core': {
            'handlers': ['console', 'debug_file', 'error_file', 'info_file'],
            'level': 'DEBUG' if ENVIRONMENT == 'development' else 'INFO',
            'propagate': False,
        },
        # Add your app-specific loggers here
        'your_app': {
            'handlers': ['console', 'debug_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console', 'production_console', 'debug_file', 'error_file'],
        'level': 'DEBUG' if ENVIRONMENT == 'development' else 'INFO',
    },
}