from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name') #Include user's first_name and last_name if there are such fields
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}, # Added 'style' for swagger
            'id': {'read_only': True} # Mark id as read_only
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nest user data as read-only

    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'balance'] #Updated with proper fields
        read_only_fields = ['id', 'user'] #User is read only, as is created during user registration