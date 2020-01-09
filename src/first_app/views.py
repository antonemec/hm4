from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from first_app.models import Student, Group


def generate_student(request):
    student = Student.generate_students()
    return HttpResponse(f'{student.get_all_info()}')


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')
