from django.shortcuts import render
from productApp.models import *

def homePage(request):
    return render(request, 'homePage.html')
def productPage(request):
    productData = productModel.objects.all()
    context ={
        'data' : productData,
    }
    return render(request, 'productPage.html', context)
def addProduct(request):
    return render(request, 'addProduct.html')