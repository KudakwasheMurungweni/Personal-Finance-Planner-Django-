# accounts/views.py
from rest_framework import viewsets, generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated  # Import permissions here!
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .serializers import (
    ProfileSerializer,
    UserSerializer,
    CustomTokenObtainPairSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView #Import TokenObtainPairView here

class UserCreateView(generics.CreateAPIView):
    """User registration endpoint (no authentication required)"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'patch'] # Limit methods

    def get_object(self):
        """Return the user's profile, or 404 if it doesn't exist"""
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user) #Filter down on the user
        return obj

    def get_queryset(self):
        """Only show the current user's profile"""
        return Profile.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance, data=request.data, partial=True) #Allow partial updates
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

    def create(self, request, *args, **kwargs):

      return Response({"detail": "Creating profiles is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED) #Not Allowed

    def destroy(self, request, *args, **kwargs):
      return Response({"detail": "Deleting profiles is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED) #Not Allowed

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):  # Use RetrieveUpdateAPIView
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  # Require authentication
    serializer_class = UserSerializer
    queryset = User.objects.all()  # Important: Override get_object

    def get_object(self):
        return self.request.user #Only allow user to edit own credentials