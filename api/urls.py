from django.urls import path

from . import views

urlpatterns = [
    # test view
    path('', views.index, name='index'),
]