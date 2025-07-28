from django.shortcuts import render,redirect, HttpResponse
from recipe.models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    recipeData = recipeModel.objects.all()
    return render(request, 'home.html', {'recipe': recipeData})
@login_required
def addRecipe(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        resumeData = recipeModel(
            image = image,
            title = title,
            description = description,
            ingredients = ingredients,
            instructions = instructions,
        )
        resumeData.save()
        return redirect('home')
    return render(request, 'addRecipe.html')
@login_required
def editRecipe(request, id):
    recipeData = recipeModel.objects.get(id=id)

    if request.method == 'POST':
        recipeData.title = request.POST.get('title')
        recipeData.description = request.POST.get('description')
        recipeData.ingredients = request.POST.get('ingredients')
        recipeData.instructions = request.POST.get('instructions')

        picture = request.FILES.get('image')
        if picture is not None:
            recipeData.image = picture
        recipeData.save()
        return redirect('home')
    return render(request, 'editRecipe.html', {'recipe': recipeData})
@login_required
def viewRecipe(request, id):
    recipeData = recipeModel.objects.get(id=id)
    return render(request, 'viewRecipe.html',{'recipe': recipeData})
@login_required
def deleteRecipe(request, id):
    recipe = recipeModel.objects.get(id=id).delete()
    return redirect('home')

def wrongPassword(request):
    return render(request, 'wrongPassword.html')
def passwordError(request):
    return render(request, 'passwordError.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return redirect('wrongPassword')
    return render(request, 'loginPage.html')

def signupPage(request):
    if request.method == 'POST':
        userName =request.POST.get('userName')
        emailAddress =request.POST.get('emailAddress')
        password =request.POST.get('password')
        confirmPassword =request.POST.get('confirmPassword')

        if password == confirmPassword:
            user = User.objects.create_user(userName, emailAddress, password)
            user.save()
            return redirect('loginPage')
        else:
            return redirect('passwordError')
    return render(request, 'signupPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

    