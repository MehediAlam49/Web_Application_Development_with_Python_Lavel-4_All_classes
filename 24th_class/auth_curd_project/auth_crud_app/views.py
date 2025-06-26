from django.shortcuts import render,redirect,HttpResponse
from auth_crud_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        full_name = request.POST.get('full_name')
        user_type = request.POST.get('role')
        dob = request.POST.get('dob')

        if password == confirm_password:
            user = customUserModel.objects.create_user(
                profile_image=profile_image,
                username=username,
                email=email,
                password=confirm_password,
                full_name=full_name,
                user_type=user_type,
                dob=dob,
            )
            return redirect('loginPage')


    return render(request, 'registerPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('wrong pass')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def home(request):
    return render(request, 'home.html')
def productList(request):
    productData = productModel.objects.all()
    return render(request, 'productList.html',{'products': productData})

@login_required
def addProduct(request):
    if request.user.user_type != 'owner':
        return redirect('productList')
    if request.method == 'POST':
        product_image = request.FILES.get('product_image')
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')

        product = productModel(
            product_image=product_image,
            product_name=product_name,
            product_description=product_description,
            product_price=product_price,

        )
        product.save()
        return redirect('productList')
    return render(request, 'addProduct.html')
@login_required
def editProduct(request,id):
    if request.user.user_type != 'owner':
        return redirect('productList')
    productData = productModel.objects.get(id=id)
    if request.method == 'POST':
        productData.product_name = request.POST.get('product_name')
        productData.product_description = request.POST.get('product_description')
        productData.product_price = request.POST.get('product_price')

        picture = request.FILES.get('product_image')
        if picture is not None:
            productData.product_image = picture
        productData.save()
        return redirect('productList')
    return render(request, 'editProduct.html', {'product': productData})
@login_required
def viewProduct(request,id):
    productData = productModel.objects.get(id=id)
    return render(request, 'viewProduct.html',{'product': productData})
@login_required
def deleteProduct(request,id):
    if request.user.user_type != 'owner':
        return redirect('productList')
    productModel.objects.get(id=id).delete()
    return redirect('productList')