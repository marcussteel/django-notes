from django.contrib import admin
from django.urls import path
from .views import forms_home

app_name = "study_forms"

urlpatterns = [
    path("forms/", forms_home, name="formshome"),
  
]
