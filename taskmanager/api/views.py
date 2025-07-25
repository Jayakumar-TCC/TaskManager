from django.shortcuts import render
from rest_framework.response import Response
from students.models import Student
from rest_framework import status
from .serializers import StudentSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Cfrom djnagoreate your views here.
@api_view(['GET','POST'])
def studentsView(request):
    if request.method=='GET':
        students = Student.objects.all()
        # students_list = list(students.values())
        serializers = StudentSerializer(students , many = True)
        return Response(serializers.data,status = status.HTTP_200_OK)

    elif request.methode=='POST':
        serializers = StudentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status = status.HTTP_201_CREATED)
        return Response(serializers.error,status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT'])
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return  Response(status = status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers = StudentSerializer(student)
        return Response(serializers.data,status = status.HTTP_200_OK)

    if request.method=='PUT':
        serializers = StudentSerializer(student,data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status = status.HTTP_200_OK)


class EmployeeDetail(APIView):

    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return  Response(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        employee = self.get_object(pk)
        serializers = StudentSerializer(employee)
        return Response(serializers.data,status = status.HTTP_200_OK)
        