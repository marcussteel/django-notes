from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import StudentForm

# Create your views here.


def forms_home(request):
    form = StudentForm()
    context = {
        'form': 'form'
    }
    
    return render(request, 'study_forms/formindex.html')

