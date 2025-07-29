from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from apiApp.models import *
from apiApp.serializers import *

# Create your views here.
@api_view(['GET'])
def studentList(request):
    if request.method == 'GET':
        student_data = StudentModel.objects.all()
        serializer = studentSerializer(student_data,many=True)

        # return response(serializer.data)
        return Response({
            "success": True,
            "message": "Student List succesfully get",
            "data": serializer.data
        },status=status.HTTP_200_OK)


@api_view(['POST'])
def addStudent(request):
    student_serializer = studentSerializer(data=request.data)
    if student_serializer.is_valid():
        student_serializer.save()
        return Response({
            "success": True,
            "message": "Student data added succesfully",
            "data": student_serializer.data
        })
    else:
        return Response({
            "success": False,
            "message": "Data not added"
        })