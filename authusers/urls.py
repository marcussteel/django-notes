from django.contrib import admin
from django.urls import path
from .views import HomeView,SpecialView

app_name = "authusers"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("special/", SpecialView.as_view(), name="home"),

]
