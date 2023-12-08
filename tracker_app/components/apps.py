"""Applications project"""

from tracker_app.components.common import INSTALLED_APPS

INSTALLED_APPS += (
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'drf_yasg',
    'api.apps.ApiConfig',
    'career_toolbox.apps.CareerToolboxConfig',
    'users.apps.UsersConfig',
    'quiz.apps.QuizConfig',
)
