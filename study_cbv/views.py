
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from msilib.schema import Class
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Student 
from .forms import StudentForm
from django.views.generic import TemplateView, ListView, DetailView,DeleteView,CreateView,UpdateView
# Create your views here.


def study_crud_view(request):
    return render(request, 'study_cbv/study_cbv.html')

class HomeView(TemplateView):
    template_name= "study_cbv/study_cbv.html"


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CBV - READ(GET)           / */
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


class StudentListRead(ListView):
    model = Student
    # context_object_name = 'students'
    # default template name : # app/modelname_list.html
    # this fits our template name no need to use this time
    # template_name = "study_cbv/study_cbv.html"
    # context_object_name = 'students'  # default context name : object_list
    # paginate_by = 10
    # queryset = Student.objects.all() or filter
    # get_queryset method for more owerfull filtering ( we can put data into get_context_data method and send template )


# def student_list_read(request):
#     student_list = Student.objects.all()
#     # student_list = get_object_or_404(Student)
    
#     context = {
#         'student_list' : student_list
#     }
#     return render(request, 'study_cbv/study_cbv.html', context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CBV - CREATE(POST)        / */
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    # default name app/modelname_form.html
    template_name = "study_cbv/student_create.html"
    success_url = reverse_lazy("cbv_model:cbv")



# def student_add(request):
#     form = StudentForm()  # boş form render edeceğiz
#     if request.method == 'POST':
#         print(request.POST)
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Student added successful")
#             print("\n-------------------Succesfully added------------------------------")
#             return redirect("cbv_model:cbv")
#     context = {
#         'form': form
#     }
#     return render(request, 'study_cbv/student_create.html', context)

    
    
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CBV - UPDATE(POST)        /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "study_cbv/student_update.html"  # default app/modelname_form.html
    success_url = '/study-cbv/home/'  # 'reverse_lazy("list")
    # pk_url_kwarg = 'id'


# def student_update(request, id):
#     student = Student.objects.get(id=id)
#     form = StudentForm(instance=student)
#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Student updated successful")
#             return redirect("cbv_model:cbv")
#     context = {
#         'form': form,
#         'student':student
#     }
#     return render(request, 'study_cbv/student_update.html', context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         CBV - DELETE(POST)        /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


class StudentDeleteView(DeleteView):
    model = Student
    # default app/modelname_confirm_delete.html
    template_name = 'study_cbv/student_delete.html'
    success_url = reverse_lazy("cbv_model:cbv")
    pk_url_kwarg = 'id'

# def student_delete(request, id):
#     # student = get_object_or_404(Student, id=id)
#     student = Student.objects.get(id=id)
#     print(student)
#     if request.method == "POST":
        
#         student.delete()
#         print("succesfully deleted")
#         return redirect("cbv_model:cbv")
#     context = {
#             'student': student,
#         }
#     return render(request, 'study_cbv/student_delete.html',context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         STUDENT DETAIL PAGE        /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

class StudentDetailView(DetailView):
    model = Student
    template_name = 'study_cbv/student_detail.html'
    pk_url_kwarg: str='id'

    # context_object_name = 'students'
    # default template name : # app/modelname_list.html
    # this fits our template name no need to use this time
    # template_name = "study_cbv/study_cbv.html"
    # context_object_name = 'students'  # default context name : object_list
    # paginate_by = 10
    # queryset = Student.objects.all() or filter
    # get_queryset method for more owerfull filtering ( we can put data into get_context_data method and send template )



# def student_detail(request, id):
#     student = Student.objects.get(id=id)
#     # print(student.profile_pic)
#     print("Student içindekiler ",bool(student.profile_pic) )
#     context = {
#         'student': student,
        
#     }
#     return render(request, 'study_cbv/student_detail.html', context)
