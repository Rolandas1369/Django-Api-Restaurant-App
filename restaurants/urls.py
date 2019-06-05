from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('restaurants', views.RestaurantView)
router.register('days', views.DayView)
router.register('menus', views.MenuView)

urlpatterns = [
    path('', include(router.urls))
]
