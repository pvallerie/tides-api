from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user profile"""
        # Validation error
        if not email:
            raise ValueError('User must enter an email address')

        # Create user
        # Use normalize_email from BaseUserManger to normalize email domain
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Hash the password
        user.set_password(password)
        # Save user to database
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""
    email = models.EmailField(max_length=225, unique=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=200)

    # objects property will reference UserManager class
    objects = UserManager()

    # declare email as unique identifier for user account instead of default username
    USERNAME_FIELD = 'email'

    def __str__(self):
        """Return user's email"""
        return self.email
    
    def get_auth_token(self):
        """Get new token for user"""
        # delete current token
        Token.objects.filter(user=self).delete()
        # generate new token
        token = Token.objects.create(user=self)
        # set users token on instance
        self.token = token.key
        # save to database
        self.save()
        return token.key
    
    def delete_token(self):
        """Delete user's token"""
        # delete current token
        Token.objects.filter(user=self).delete()
        # delete token from user's instance
        self.token = None
        # save to database
        self.save()
        return self