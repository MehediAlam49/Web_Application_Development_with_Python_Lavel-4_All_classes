from django import forms
from library_app.models import *


class LibraryForm(forms.ModelForm):
    class Meta:
        model = LibraryModel
        fields = '__all__'