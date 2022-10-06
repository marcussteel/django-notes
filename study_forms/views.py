from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import StudentForm,Student
from django.contrib import messages

# Create your views here.


def forms_home(request):
    print(request.POST)
    print(request.FILES)
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # student_data = {
            #     "first_name": form.cleaned_data.get('first_name'),
            #     "last_name": form.cleaned_data.get('last_name'),
            #     "number": form.cleaned_data.get('number'),
            #     "description": form.cleaned_data.get('description'),
            #     "is_active": form.cleaned_data.get("is_active"),
            #     "profile_pic": form.cleaned_data.get('profile_image'),
            # }
            # student = Student(**student_data)
            # student.save()
            form.save()
            messages.success(request, "Student added successful")
            return redirect('study_forms:student')

    context = {
        'form': form
    }
    
    return render(request, 'study_forms/formindex.html',context)


def student(request):
    student= Student()
    context = {
        'student' : student,
    }

    return render(request, 'study_forms/student.html',context)
