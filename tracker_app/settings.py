from decouple import config
from split_settings.tools import include


SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = ['127.0.0.1']
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
