from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
# Create your views here.
def students(request):
    students = Student.object.all()
    print(students)
    return JsonResponse(students)