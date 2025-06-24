from django.shortcuts import render
from productApp.models import *

# Create your views here.
def home(request):
    customerData = customerModel.objects.all()
    context = {'data': customerData}
    return render(request, 'home.html', context)
def product(request):
    productData = productModel.objects.all()
    context = {'data': productData}
    return render(request, 'product.html', context)
def addProduct(request):
    return render(request, 'addProduct.html')
def addCustomer(request):
    return render(request, 'addCustomer.html')
def customer(request):
    return render(request, 'customer.html')