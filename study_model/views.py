from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def study_model_view(request):
    return HttpResponse("This is study-model page")
