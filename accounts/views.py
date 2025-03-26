# accounts/views.py
from rest_framework import viewsets, generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import Profile
from .serializers import (
    ProfileSerializer, 
    UserSerializer, 
    CustomTokenObtainPairSerializer  # Add this import
)

class UserCreateView(generics.CreateAPIView):
    """User registration endpoint (no authentication required)"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """Only show the current user's profile"""
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically associate profile with logged-in user"""
        serializer.save(user=self.request.user)

# New Custom Token Obtain Pair View
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer