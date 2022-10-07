from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Student 
from .forms import StudentForm
# Create your views here.


def study_crud_view(request):
    return render(request, 'study_crud/study_crud.html')



# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CRUD - READ(GET)           / */
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

def student_list_read(request):
    student_list = Student.objects.all()
    # student_list = get_object_or_404(Student)
    
    context = {
        'student_list' : student_list
    }
    return render(request, 'study_crud/study_crud.html', context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CRUD - CREATE(POST)        / */
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def student_add(request):
    form = StudentForm()  # boş form render edeceğiz
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            print("\n-------------------Succesfully added------------------------------")
            return redirect("crud_model:crud")
    context = {
        'form': form
    }
    return render(request, 'study_crud/student_create.html', context)

    
    
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CRUD - UPDATE(POST)        /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successful")
            return redirect("crud_model:crud")
    context = {
        'form': form,
        'student':student
    }
    return render(request, 'study_crud/student_update.html', context)



# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CRUD - DELETE(POST)        /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    print(student)
    if request.method == "POST":
        
        student.delete()
        print("succesfully deleted")
        return redirect("crud_model:crud")
    context = {
            'student': student,
        }
    return render(request, 'study_crud/student_delete.html',context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         STUDENT DETAIL PAGE        /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

def student_detail(request, id):
    student = Student.objects.get(id=id)
    # print(student.profile_pic)
    print("Student içindekiler ",bool(student.profile_pic) )
    context = {
        'student': student,
        
    }
    return render(request, 'study_crud/student_detail.html', context)
