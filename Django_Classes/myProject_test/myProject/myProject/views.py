from django.shortcuts import render
from myApp.models import *

def viewStudent(request):
    studentData=studentModel.objects.all()
    context={
        'data':studentData,
    }
    return render(request, 'viewStudent.html',context)
def homePage(request):
    return render(request, 'homePage.html')
def contactPage(request):
    return render(request, 'contactPage.html')
def newsPage(request):
    return render(request, 'newsPage.html')
def aboutPage(request):
    newstudentData=newstudentModel.objects.all()
    context={
        'data':newstudentData,
    }
    return render(request, 'aboutPage.html',context)


