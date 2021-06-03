from django.urls import path

from .views import index, SignUp

urlpatterns = [
    # test view
    path('', index, name='index'),
    # auth views
    path('sign-up/', SignUp.as_view(), name='sign-up'),
]