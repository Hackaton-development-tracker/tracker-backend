from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SpecializationViewSet, CustomUserViewSet

app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register(r'specialization', SpecializationViewSet,
                   basename='specialization')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
