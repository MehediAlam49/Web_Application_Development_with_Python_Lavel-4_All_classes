from django import forms
from portal.models import *


class TeachrForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['teacher_name','last_education','phone','address']
   