from django.contrib import admin
from django.urls import path
from .views import views_home, views_page

app_name = "study_views"

urlpatterns = [
    path("viewshome/", views_home, name="viewshome"),
    path("viewspage/", views_page, name="viewspage")
]
