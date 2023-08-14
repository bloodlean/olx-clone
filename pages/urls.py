from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('electronics/', electronics, name='electronics'),
    path('electronics/<pk>/', sale_detail, name='sale_detail'),
    path('transport/', transport, name='transport'),
    path('transport/<pk>/', transport_detail, name='transport_detail'),
    path('furniture/', furniture, name='furniture'),
    path('furniture/<pk>/', furniture_detail, name='furniture_detail'),
    path('clothes/', clothes, name='clothes'),
    path('clothes/<pk>/', clothes_detail, name='clothes_detail'),
    path('sport/', sport, name='sport'),
    path('sport/<pk>/', sport_detail, name='sport_detail'),
]