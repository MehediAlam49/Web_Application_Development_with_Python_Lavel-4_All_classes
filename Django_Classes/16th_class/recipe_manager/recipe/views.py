from django.shortcuts import render, redirect
from recipe.models import *

# Create your views here.
def home(request):
    recipeData = recipeModel.objects.all()
    return render(request, 'home.html', {'recipes': recipeData})
def addRecipe(request):
    if request.method == 'POST':
        recipeData = recipeModel(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            ingredients = request.POST.get('ingredients'),
            instructions = request.POST.get('instructions'),
            image = request.FILES.get('image'),

        )
        recipeData.save()
        return redirect('home')
    return render(request, 'addRecipe.html')
def deleteRecipe(request,id):
    recipe = recipeModel.objects.get(id=id).delete()
    return redirect('home')
def editRecipe(request,id):
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
    return render(request, 'editRecipe.html',{'recipe': recipeData})

def viewRecipe(request,id):
    recipeData = recipeModel.objects.get(id=id)
    return render(request, 'viewRecipe.html',{'recipe':recipeData})