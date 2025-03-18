# accounts/serializers.py
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Never expose passwords!
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nest user data as read-only
    
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'currency', 'created_at']
        read_only_fields = ['id', 'created_at']