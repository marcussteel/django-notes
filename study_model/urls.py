from django.contrib import admin
from django.urls import path
from .views import study_model_view

app_name = "study_model"
urlpatterns = [
    path("home/", study_model_view, name="study")
]
