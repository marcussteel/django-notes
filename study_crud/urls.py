from django.contrib import admin
from django.urls import path
from .views import student_delete, study_crud_view, student_list_read, student_add,student_update,student_detail

app_name = "crud_model"
urlpatterns = [
    path("home/", student_list_read, name="crud" ),
    path("add/", student_add, name="student_add" ),
    path("update/<int:id>", student_update, name="update" ),
    path("delete/<int:id>", student_delete, name="delete" ),
    # path("delete/<int:id>", student_delete, name="delete" ),
    path("detail/<int:id>", student_detail, name="detail" ),
]