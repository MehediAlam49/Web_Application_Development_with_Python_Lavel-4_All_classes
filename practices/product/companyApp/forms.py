from django import forms
from companyApp.models import *


class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = '__all__'
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        
class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        