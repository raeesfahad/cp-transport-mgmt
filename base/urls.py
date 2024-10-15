from django.contrib import admin
from django.urls import path, include
from .views import index, login

urlpatterns = [
    path( "", index, name="home"),
    path( "login", login, name="login")
]