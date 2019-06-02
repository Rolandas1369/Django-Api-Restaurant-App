from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    components = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class WeekDay(models.Model):
    weekday = models.CharField(max_length=100)

    def __str__(self):
        return self.weekday

class Choice(models.Model):
    menu = models.ForeignKey(Menu, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text
