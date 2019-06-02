from django.urls import path

from .apiviews import RestaurantList, MenuList, WeekDayList


urlpatterns = [
    path("restaurants/", RestaurantList.as_view(), name="restaurant_list"),
    path("restaurants/<int:pk>/menus/", MenuList.as_view(), name="menu_list"),
    path("restaurants/<int:pk>/menus/weekday/", WeekDayList.as_view(), name="day_list"),
    #path("restaurants/<int:pk>/menu/<int:choice_pk>/vote/", )
    #path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]
