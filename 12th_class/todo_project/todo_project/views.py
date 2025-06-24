from django.shortcuts import render,redirect
from tasks.models import *
import random

# def home(request):
#     query = {'userData': userModel.objects.all()}
#     return render(request, 'home.html',query)
def home(request):
    userData = userModel.objects.all()
    return render(request, 'home.html',{'userData': userData})

def addTask(request):
    if request.method == 'POST':
        task = taskModel(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            dueDate = request.POST.get('dueDate'),
        )
        task.save()
        return redirect('taskList')
    return render(request, 'addTask.html')
def editTask(request,id):
    task = taskModel.objects.get(id=id)
    query={'taskData': task}
    if request.method == 'POST':
        task = taskModel(
            id = id,
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            dueDate = request.POST.get('dueDate'),
        )
        task.save()
        return redirect('taskList')
    return render(request, 'editTask.html',query)
def deleteTask(request,id):
    task = taskModel.objects.get(id=id).delete()
    return redirect('taskList')
def viewTask(request):
    return render(request, 'viewTask.html')
def taskList(request):
    query = {'taskData': taskModel.objects.all()}
    return render(request, 'taskList.html',query)




def addUser(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        full_name = fname+ ' ' +lname
        digit = random.randint(100, 999)
        userName = fname + str(digit)
        
        user = userModel(
            fname = fname,
            lname = lname,
            full_name =full_name,
            userName = userName
        )
        user.save()
        return redirect('/')
    return render(request, 'addUser.html')

