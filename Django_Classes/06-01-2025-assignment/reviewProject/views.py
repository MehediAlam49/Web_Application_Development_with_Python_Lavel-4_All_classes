from django.shortcuts import render 
from django.shortcuts import redirect

from reviewApp.models import *

def Home(request):
    return render(request,'Home.html')


def AddStudent(request):
    if request.method=='POST':
        student=StudentModel(
            Student_Name=request.POST.get("studentName"),
            Department_Name=request.POST.get("departmentName"),
            City_Name=request.POST.get("city"),
            Student_Age=request.POST.get("studentAge"),

        )
        student.save()
        return redirect("StudentList")
    return render(request,"AddStudent.html")



def StudentList(request):
    studentData = StudentModel.objects.all()
    context={
        'studentList' : studentData,
    }

    return render(request,'StudentList.html',context)



def AddTeacher(request):
    if request.method=='POST':
        teacher=TeacherModel(
            Teacher_Name=request.POST.get("teacherName"),
            Department_Name=request.POST.get("departmentName"),
            Email=request.POST.get("email"),
            Designation=request.POST.get("designation"),

        )
        teacher.save()
        return redirect("TeacherList")
    return render(request,"AddTeacher.html")



def TeacherList(request):
    teacherData = TeacherModel.objects.all()
    context={
        'teacherList' : teacherData,
    }

    return render(request,'TeacherList.html',context)



def AddCourse(request):
    if request.method=='POST':
        course=CourseModel(
            Course_Name=request.POST.get("courseName"),
            Course_Number=request.POST.get("courseNumber"),
            Course_Credit=request.POST.get("courseCredit"),
            Course_Duration=request.POST.get("courseDuration"),

        )
        course.save()
        return redirect("CourseList")
    return render(request,"AddCourse.html")



def CourseList(request):
    courseData = CourseModel.objects.all()

    context={
        'courseList' : courseData,
    }

    return render(request,'CourseList.html',context)



def deleteStudent(request,myid):
   
    students=StudentModel.objects.get(id=myid)

    students.delete()

    return redirect("StudentList")


def deleteTeacher(request,myid):
   
    teachers=TeacherModel.objects.get(id=myid)

    teachers.delete()

    return redirect("TeacherList")



def deleteCourse(request,myid):
   
    courses=CourseModel.objects.get(id=myid)

    courses.delete()

    return redirect("CourseList")



def editStudent(request,myid):
   
    student=StudentModel.objects.get(id=myid)
    contex={
        'data':student
    }


    if request.method=='POST':
        student=StudentModel(
            id=myid,
            Student_Name=request.POST.get("studentName"),
            Department_Name=request.POST.get("departmentName"),
            City_Name=request.POST.get("city"),
            Student_Age=request.POST.get("studentAge"),

        )
        student.save()
        return redirect("StudentList")
    


    return render(request,"editStudent.html",contex)

def editTeacher(request,myid):
   
    teacher=TeacherModel.objects.get(id=myid)
    contex={
        'data':teacher
    }

    if request.method=='POST':
        teacher=TeacherModel(
            id=myid,
            Teacher_Name=request.POST.get("teacherName"),
            Department_Name=request.POST.get("departmentName"),
            Email=request.POST.get("email"),
            Designation=request.POST.get("designation"),

        )
        teacher.save()
        return redirect("TeacherList")


    return render(request,"editTeacher.html",contex)



def editCourse(request,myid):
   
    course=CourseModel.objects.get(id=myid)
    contex={
        'data':course
    }

    if request.method=='POST':
        course=CourseModel(
            id=myid,
            Course_Name=request.POST.get("CourseName"),
            Course_Number=request.POST.get("Course_Number"),
            Course_Credit=request.POST.get("Course_Credit"),
            Course_Duration=request.POST.get("Course_Duration"),

        )
        course.save()
        return redirect("CourseList")


    return render(request,"editCourse.html",contex)

