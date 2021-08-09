from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/greet', views.greet)
]
