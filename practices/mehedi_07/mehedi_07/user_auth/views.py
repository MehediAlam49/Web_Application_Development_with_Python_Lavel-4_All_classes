from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def registerPage(request):
    return render(request, registerPage.html)