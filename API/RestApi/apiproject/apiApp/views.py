from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from apiApp.models import *
from apiApp.serializers import *
from rest_framework.views import APIView

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
    


class TeacherAPIView(APIView):
    def get(self,request):
        teacher_data = TeacherModel.objects.all()
        serializer = TeacherSerializer(teacher_data, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class TeacherDetails(APIView):
    def put(self, request,id):
        if not id:
            return Response({
                'message': 'Plesase must be ad id for put method'
            },status=status.HTTP_400_BAD_REQUEST)
        try:
            teacher = TeacherModel.objects.get(id=id)
        except TeacherModel.DoesNotExist:
            return Response({'message':'Teacher does not exist'})
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "success": True,
            "message": "Student data added succesfully",
            "data": serializer.data
        })
        else:
            return Response(serializer.errors)
    
    def delete(self,request,id):
        try:
            teacher = TeacherModel.objects.get(id=id)
        except TeacherModel.DoesNotExist:
            return Response({'message': 'Teacher does not exit'})
        teacher.delete()
        return Response({'message': 'Teacher delete successfully'})
        
        