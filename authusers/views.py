from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'authusers/index.html'

class SpecialView(TemplateView):
    template_name = 'authusers/special.html'
