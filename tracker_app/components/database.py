"""Database config project"""
import os
from pathlib import Path

from decouple import config

from tracker_app.settings import DEBUG


BASE_DIR = Path(__file__).resolve().parent.parent

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': '172.18.0.2',
            'PORT': config('DB_PORT', 5432),
        }
    }
