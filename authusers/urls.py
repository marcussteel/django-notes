from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    HomeView,
    SpecialView,
    password_change,
    register,
    special,
    user_logout
)

app_name = "authusers"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("special/", special, name="special"),
    path("special/", login_required( SpecialView.as_view()), name="special2"),
    path("register/",register , name="register"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"), name="password_change"),  
        # password_change/ ya istek geldiğinde bizi  auth_views.PasswordChangeView.as_view a gönder ama bu da template_name="registration/password_change.html içinde demişiz.
        #  from django.contrib.auth import views as auth_views
        #veya stteingste authusers yani override edilecek yeni html lerin app ini en üste taşı.
    path('logout/', user_logout,name='logout'),

]
