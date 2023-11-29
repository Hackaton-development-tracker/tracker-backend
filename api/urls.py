from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register("users", UserViewSet, basename="users")


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
