
from django.urls import path, include
from rest_framework import routers
from .views import homepageview, roompageview



urlpatterns = [
    path("", homepageview),
    path("room/", roompageview, name="room"),
]