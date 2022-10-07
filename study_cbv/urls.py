from django.contrib import admin
from django.urls import path
from .views import student_delete, study_crud_view, student_list_read, student_add,student_update,student_detail

app_name = "cbv_model"
urlpatterns = [
    path("home/", student_list_read, name="cbv" ),
    path("add/", student_add, name="cbvstudent_add" ),
    path("update/<int:id>", student_update, name="cbvupdate" ),
    path("delete/<int:id>", student_delete, name="cbvdelete" ),
    path("delete/<int:id>", student_delete, name="cbvdelete" ),
    path("detail/<int:id>", student_detail, name="cbvdetail" ),
]