from django.urls import path
from . import views

urlpatterns = [
    path('forms/wheel-specifications', views.wheel_specifications),
]
