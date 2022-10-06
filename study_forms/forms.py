from dataclasses import fields
import re
from django import forms

from study_model.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name","last_name","number","description","is_active"]
