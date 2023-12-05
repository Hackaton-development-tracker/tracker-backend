from decouple import config
from django.core.management.utils import get_random_secret_key
from split_settings.tools import include

SECRET_KEY = get_random_secret_key()
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'tracker_app.urls'

# Пока что не нужна, но после генерации
# локализации раскоментим и поправим
# LOCALE_PATHS = ['/locale']


# Base settings
include('components/common.py')

# Some APPs project
include('components/apps.py')

# Database connection
include('components/database.py')

# Localization
include('components/localization.py')

# Auth password validation
include('components/auth_pass_validators.py')
