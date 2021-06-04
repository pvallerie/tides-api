from django.urls import path

from .views import index, SignUp, SignIn

urlpatterns = [
    # test view
    path('', index, name='index'),
    # auth views
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
]