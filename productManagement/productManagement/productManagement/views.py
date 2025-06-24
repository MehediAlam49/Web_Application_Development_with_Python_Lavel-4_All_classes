from django.shortcuts import render

def homePage(request):
    return render(request, 'homePage.html')
def productPage(request):
    return render(request, 'productPage.html')
def addProduct(request):
    return render(request, 'addProduct.html')
def master(request):
    return render(request, 'master.html')