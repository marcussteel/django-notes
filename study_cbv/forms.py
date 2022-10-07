from dataclasses import fields
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # '__all__' olarak da yazabiliriz ama tüm biilgileri  göndermeye gerek yok
        fields = ["first_name", "last_name", "number","description", "is_active", "profile_pic"]
        labels = {"first_name": "Name"}  # görünümü değişiyor
