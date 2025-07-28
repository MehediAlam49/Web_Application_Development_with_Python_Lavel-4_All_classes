from django import forms
from LibraryApp.models import BookModel

class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'isbn', 'quantity']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter isbn'
            }),
            
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity'
            }),
            
            # 'created_at': forms.DateInput(attrs={
            #     'class': 'form-control',
            #     'type': 'date'
            # }),
        }