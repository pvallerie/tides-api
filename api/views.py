from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import status, generics
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .serializers import UserSerializer, UserSignUpSerializer, CreateLocationSerializer
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

# Sign In
class SignIn(generics.CreateAPIView):
    """View to sing User in"""
    # override auth/permission classes
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

    def post(self, request):
        creds = request.data['credentials']
        print(creds)
        user = authenticate(request, email=creds['email'], password=creds['password'])
        # If user is authenticated
        if user is not None:
            # And they're active
            if user.is_active:
                # Log them in
                login(request, user)
                # Send response with user's token
                return Response({
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'token': user.get_auth_token()
                    }
                })
            # If they're not active, send 400
            else:
                return Response({ 'msg': 'The account is inactive.' }, status=status.HTTP_400_BAD_REQUEST)
        # If they're not authenticated
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Sign Out
class SignOut(generics.DestroyAPIView):
    """Sign user out"""
    def delete(self, request):
        # Remove user's token from db
        request.user.delete_token()
        # Logout (removing session data)
        logout(request)
        # Send logout confirmation to user
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create Location
class CreateLocation(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=CreateLocationSerializer

    def post(self, request):
        """Create request"""
        print('REQUEST DATA-------->', request.data)
        request.data['location']['owner'] = request.user.id
        location = CreateLocationSerializer(data=request.data['location'])
        if location.is_valid():
            location.save()
            return Response({ 'location': location.data }, status=status.HTTP_201_CREATED)
        return Response(location.errors, status=status.HTTP_400_BAD_REQUEST)

# ChangeLocation
# class ChangeLocation(generics.UpdateAPIView):
#     """Updates user's location"""
#     def partial_update(self, request):
#         print('USER----------->:', request.location)
#         user = request.user
#         location = request.location
#         # update location in database
#         user.set_location(self, location)

#         return Response({
#                     'user': {
#                         'id': user.id,
#                         'email': user.email,
#                         'token': user.get_auth_token(),
#                         'location': user.location
#                     }
#                 })
