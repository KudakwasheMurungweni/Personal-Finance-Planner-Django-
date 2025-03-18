# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, UserCreateView  # Make sure UserCreateView is imported

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),  # Registration endpoint
    path('', include(router.urls)),  # Profile endpoints
]