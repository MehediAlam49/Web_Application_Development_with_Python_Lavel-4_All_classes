from django import forms
from formApp.models import *

class UserInfoForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()

class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = BasicInfoModel
        fields = ['full_name','email','phone','address','profile']
   