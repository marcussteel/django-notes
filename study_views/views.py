from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def views_home(request):
    return HttpResponse("This page is for Study_Views")

def views_page(request):

    return render(request, "study_views/homepage.html")