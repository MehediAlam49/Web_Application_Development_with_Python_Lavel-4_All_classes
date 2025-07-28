from django import forms
from portal.models import TeacherModel

class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ['teacher_name', 'last_education', 'phone', 'address']
        widgets = {
            'teacher_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'last_education': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Highest qualification (e.g. MSc, B.Ed)'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'rows': 3
            }),
        }
