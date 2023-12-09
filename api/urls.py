from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, SpecializationViewSet, TestViewSet

app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('specialization', SpecializationViewSet,
                   basename='specialization')
router_v1.register(r'tests', TestViewSet, basename='test')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]