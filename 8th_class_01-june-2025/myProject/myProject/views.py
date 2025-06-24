from django.shortcuts import render,redirect
from myApp.models import *

def home(request):
    return render(request, 'home.html')
def addStudent(request):
    if request.method == 'POST':
        student=studentModel(
            name = request.POST.get('name'),
            department = request.POST.get('department'),
            city = request.POST.get('city'),
            age = request.POST.get('age'),

        )
        student.save()
        return redirect('studentList')
    return render(request, 'addStudent.html')

def addTeacher(request):
    if request.method == 'POST':
        teacher=teacherModel(
            name = request.POST.get('name'),
            designation = request.POST.get('designation'),
            city = request.POST.get('city'),
            age = request.POST.get('age'),

        )
        teacher.save()
        return redirect('teacherList')
    return render(request, 'addTeacher.html')

def addCourse(request):
    if request.method == 'POST':
        course=courseModel(
            title = request.POST.get('title'),
            course_code = request.POST.get('course_code'),
            semester = request.POST.get('semester'),
            duration = request.POST.get('duration'),

        )
        course.save()
        return redirect('courseList')
    return render(request, 'addCourse.html')



def studentList(request):
    context={'data': studentModel.objects.all()}
    return render(request, 'studentList.html',context)

def teacherList(request):
    context={'data': teacherModel.objects.all()}
    return render(request, 'teacherList.html',context)

def courseList(request):
    context={'data': courseModel.objects.all()}
    return render(request, 'courseList.html',context)

# course Actions
def editCourse(request,myid):
    course = courseModel.objects.get(id=myid)
    context={'courseData': course}
    if request.method == 'POST':
        course=courseModel(
            id = myid,
            title = request.POST.get('title'),
            course_code = request.POST.get('course_code'),
            semester = request.POST.get('semester'),
            duration = request.POST.get('duration'),

        )
        course.save()
        return redirect('courseList')
    return render(request, 'editCourse.html',context)
def deleteCourse(request,myid):
    course = courseModel.objects.get(id=myid).delete()
    return redirect('courseList')
def viewCourse(request,myid):
    course = courseModel.objects.get(id=myid)
    return redirect('courseList')

# Student Actions
def editStudent(request,myid):
    student = studentModel.objects.get(id=myid)
    context = {'studentData': student}
    if request.method == 'POST':
        student=studentModel(
        id = myid,
        name = request.POST.get('name'),
        department = request.POST.get('department'),
        city = request.POST.get('city'),
        age = request.POST.get('age'),

        )
        student.save()
        return redirect('studentList')
    return render(request, 'editStudent.html',context)
def deleteStudent(request,myid):
    student = studentModel.objects.get(id=myid).delete()
    return redirect('studentList')
def viewStudent(request,myid):
    student = studentModel.objects.get(id=myid)
    return redirect('studentList')

# Teacher Actions
def editTeacher(request,myid):
    teacher = teacherModel.objects.get(id=myid)
    context = {'teacherData': teacher}
    return render(request, 'editTeacher.html',context)
def deleteTeacher(request,myid):
    teacher = teacherModel.objects.get(id=myid).delete()
    return redirect('teacherList')
def viewTeacher(request,myid):
    teacher = teacherModel.objects.get(id=myid)
    return redirect('teacherList')