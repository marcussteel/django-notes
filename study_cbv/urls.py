from django.contrib import admin
from django.urls import path
from .views import HomeView, StudentListRead,StudentDetailView, StudentCreateView,StudentUpdateView,StudentDeleteView

app_name = "cbv_model"
urlpatterns = [
    # path("home/", student_list_read, name="cbv" ),
    path("home/", StudentListRead.as_view(), name="cbv" ),
    # path("home/", HomeView.as_view(), name="cbv" ),


    path("add/", StudentCreateView.as_view(), name="cbvstudent_add" ),
    # path("add/", student_add, name="cbvstudent_add" ),

    path("update/<int:pk>", StudentUpdateView.as_view(), name="cbvupdate" ),

    # path("update/<int:id>", student_update, name="cbvupdate" ),

    path("delete/<int:id>", StudentDeleteView.as_view(), name="cbvdelete" ),
    # path("delete/<int:id>", student_delete, name="cbvdelete" ),

    path("detail/<int:id>", StudentDetailView.as_view(), name="cbvdetail" ),
    # path("detail/<int:id>", student_detail, name="cbvdetail" ),
]