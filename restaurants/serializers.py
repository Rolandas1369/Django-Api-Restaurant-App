from rest_framework import serializers

from .models import Restaurant
from .models import Menu
from .models import WeekDay

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

class WeekDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeekDay
        fields = '__all__'    
