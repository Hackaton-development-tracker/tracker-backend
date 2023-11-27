"""Applications project"""

from tracker_app.components.common import INSTALLED_APPS

INSTALLED_APPS += (
    'api.apps.ApiConfig',
    'career_toolbox.apps.CareerToolboxConfig',
    'users.apps.UsersConfig',
)
