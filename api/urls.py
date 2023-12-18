from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CourseViewSet, CustomUserViewSet, KnowledgeBaseViewSet,
                    ProjectViewSet, SpecializationViewSet, TestViewSet,
                    UserSkillViewSet)

app_name = 'api'
router_v1 = DefaultRouter()

router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('specialization', SpecializationViewSet,
                   basename='specialization')
router_v1.register('tests', TestViewSet, basename='test')
router_v1.register('courses', CourseViewSet, basename='course')
router_v1.register('user_skills', UserSkillViewSet, basename='user_skills')
router_v1.register('knowledges', KnowledgeBaseViewSet, basename='knowledges')
router_v1.register('projects', ProjectViewSet, basename='projects')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls.authtoken')),
]
