from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Day(models.Model):
    day = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.day

class Menu(models.Model):
    menu = models.CharField(max_length=100)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu
