from django.urls import path
from companyApp.views import *

urlpatterns = [
    path('',createCompany, name='createCompany'),
    path('companyList/',companyList, name='companyList'),
    path('editCompany/<str:id>',editCompany, name='editCompany'),
    path('deleteCompany/<str:id>',deleteCompany, name='deleteCompany'),
    
    
    path('createProduct/',createProduct, name='createProduct'),
    path('productList/',productList, name='productList'),
    path('editProduct/<str:id>',editProduct, name='editProduct'),
    path('deleteProduct/<str:id>',deleteProduct, name='deleteProduct'),
    
    
    path('createJob/',createJob, name='createJob'),
    path('jobList/',jobList, name='jobList'),
    path('editJob/<str:id>',editJob, name='editJob'),
    path('deleteJob/<str:id>',deleteJob, name='deleteJob'),
    
    
    path('createEmployee/',createEmployee, name='createEmployee'),
    path('employeeList/',employeeList, name='employeeList'),
    path('editEmployee/<str:id>',editEmployee, name='editEmployee'),
    path('deleteEmployee/<str:id>',deleteEmployee, name='deleteEmployee'),
]

