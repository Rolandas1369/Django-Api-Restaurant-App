from django.shortcuts import render
from rest_framework import viewsets

from .models import Restaurant, Menu, Day
from .serializers import RestaurantSerializer, MenuSerializer, DaySerializer


class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class DayView(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
