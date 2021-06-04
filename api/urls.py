from django.urls import path

from .views import index, SignUp, SignIn, SignOut, CreateLocation, ChangeLocation

urlpatterns = [
    # test view
    path('', index, name='index'),
    # auth views
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('locations/', CreateLocation.as_view(), name='create-location'),
    path('locations/<int:pk>/', ChangeLocation.as_view(), name='change-location'),
]