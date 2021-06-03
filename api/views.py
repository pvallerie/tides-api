from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import render
from django.http import HttpResponse

from .serializers import UserSerializer, UserSignUpSerializer
from .models import User

# test view
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Sign Up
class SignUp(generics.CreateAPIView):
    """View to sign up new User"""
    # override auth/permission classes
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSignUpSerializer

    def post(self, request):
        # Validate request data using serializer
        user = UserSignUpSerializer(data=request.data['credentials'])
        # If data validated, create user
        if user.is_valid():
            created_user = UserSerializer(data=user.data)

            if created_user.is_valid():
                # Save user and send response
                created_user.save()
                return Response({ 'user': created_user.data }, status=status.HTTP_201_CREATED)
            else:
                return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
