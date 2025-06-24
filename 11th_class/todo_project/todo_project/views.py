from django.shortcuts import render,redirect
from tasks.models import *

def home(request):
    return render(request, 'home.html')
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