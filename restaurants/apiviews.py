from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Restaurant, Menu, WeekDay
from .serializers import RestaurantSerializer, MenuSerializer, WeekDaySerializer


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class WeekDayList(generics.ListCreateAPIView):
    queryset = WeekDay.objects.all()
    serializer_class = WeekDaySerializer
