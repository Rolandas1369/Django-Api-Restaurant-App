from rest_framework import serializers

from .models import Restaurant
from .models import Menu
from .models import Day

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'url', 'name')

class MenuSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'url', 'menu', 'day', 'restaurant')

class DaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Day
        fields = ('id', 'url', 'day' ,'restaurant')
