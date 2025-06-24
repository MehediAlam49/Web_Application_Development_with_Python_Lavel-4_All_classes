from django.shortcuts import render,redirect
from product.models import *


def home(request):
    return render(request, 'home.html')
def productList(request):
    context ={'productData': productModel.objects.all()}
    return render(request, 'productList.html',context)
def addProduct(request):
    if request.method =='POST':
        product =productModel(
            product_name = request.POST.get('product_name'),
            category = request.POST.get('category'),
            quantity = request.POST.get('quantity'),
            price = request.POST.get('price'),
            status = request.POST.get('status')
        )
        product.save()
        return redirect('productList')
    return render(request, 'addProduct.html')

def deleteProduct(request,myid):
    product=productModel.objects.get(id =myid).delete()
    return redirect('productList')

def editProduct(request,myid):
    product=productModel.objects.get(id =myid)
    return redirect('productList')

def viewProduct(request,myid):
    product=productModel.objects.get(id =myid)
    return redirect('productList')
