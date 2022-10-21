from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path(r'', include(router.urls), name='users'),
]