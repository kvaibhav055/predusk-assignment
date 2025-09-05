from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProjectViewSet, SkillViewSet, WorkViewSet, health


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'work', WorkViewSet)


urlpatterns = [
path('health/', health),
path('', include(router.urls)),
]
