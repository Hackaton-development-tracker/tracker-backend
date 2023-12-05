"""Database config project"""
import os
from pathlib import Path

from decouple import config

ENVIRONMENT = config('ENVIRONMENT')
BASE_DIR = Path(__file__).resolve().parent.parent


if ENVIRONMENT == 'testing':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': 'localhost',
            'PORT': config('DB_PORT', 5432),
        }
    }
