from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Location

# from .models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer to be used for User creation"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }
    
    # Method for User model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserSignUpSerializer(serializers.Serializer):
    """Serializer to be used for signing up"""
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # check for pw and pw confirmation
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation')

        # check whether pw and pw confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your password and password confirmation match')

        # if we pass checks, return data
        return data

class CreateLocationSerializer(serializers.ModelSerializer):
    """Creates location for user"""
    class Meta:
        model = Location
        fields = ('name', 'owner', 'id')

class GetLocationSerializer(serializers.ModelSerializer):
    """Get location"""
    owner = UserSerializer()
    class Meta:
        model = Location
        fields = ('name', 'owner', 'id')
        