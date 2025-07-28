from django import forms

from .models import JobModel

class JobModelForm(forms.ModelForm):

    class Meta:
        model = JobModel
        fields = ('job_title', 'description', 'salary', 'location', 'deadline')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job description',
                'rows': 4
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job requirements',
                'rows': 4
            }),
            'sallary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary amount'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

