from django.urls import path
from . import views

urlpatterns = [
    path('', views.products),
    path('products/', views.products),
    path('products/new/', views.new)
]
