from django.shortcuts import render,redirect,get_object_or_404
from companyApp.forms import *
from companyApp.models import *

# Create your views here.
def createCompany(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companyList')
    else:
        form = CompanyForm()
    return render(request, 'createCompany.html',{'form':form})

def companyList(request):
    company_data = CompanyModel.objects.all()
    return render(request, 'companyList.html',{'company_data':company_data})

def editCompany(request,id):
    data = get_object_or_404(CompanyModel, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('companyList')
    else:
        form = CompanyForm(instance=data)
    return render(request, 'editCompany.html',{'form':form})
def deleteCompany(request,id):
    get_object_or_404(CompanyModel, id=id).delete()
    return redirect('companyList')



def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productList')
    else:
        form = ProductForm()
    return render(request, 'createProduct.html',{'form':form})

def productList(request):
    product_data = ProductModel.objects.all()
    return render(request, 'productList.html',{'product_data':product_data})

def editProduct(request,id):
    data = get_object_or_404(ProductModel, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('productList')
    else:
        form = ProductForm(instance=data)
    return render(request, 'editProduct.html',{'form':form})
def deleteProduct(request,id):
    get_object_or_404(ProductModel, id=id).delete()
    return redirect('productList')


def createJob(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobList')
    else:
        form = JobForm()
    return render(request, 'createjob.html',{'form':form})

def jobList(request):
    job_data = JobModel.objects.all()
    return render(request, 'jobList.html',{'job_data':job_data})

def editJob(request,id):
    data = get_object_or_404(JobModel, id=id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('jobList')
    else:
        form = JobForm(instance=data)
    return render(request, 'editJob.html',{'form':form})
def deleteJob(request,id):
    get_object_or_404(JobModel, id=id).delete()
    return redirect('jobList')


def createEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeList')
    else:
        form = EmployeeForm()
    return render(request, 'createEmployee.html',{'form':form})

def employeeList(request):
    employee_data = EmployeeModel.objects.all()
    return render(request, 'employeeList.html',{'employee_data':employee_data})

def editEmployee(request,id):
    data = get_object_or_404(EmployeeModel, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('employeeList')
    else:
        form = EmployeeForm(instance=data)
    return render(request, 'editJob.html',{'form':form})
def deleteEmployee(request,id):
    get_object_or_404(EmployeeModel, id=id).delete()
    return redirect('employeeList')