# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('homer/', views.restaurant1, name='restaurant1'),
    path('', views.home, name='home'),
    path('homer2/', views.foodstreet, name='foodstreet'),
    path('homer3/', views.luxurydining, name='luxurydining'),
    path('shoppingmall1/', views.shoppingmall1, name='shoppingmall1'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('luxurymall/', views.luxurymall, name='luxurymall'),
]

