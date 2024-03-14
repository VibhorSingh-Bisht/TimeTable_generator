from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "Add Teacher.html")#, context={'peoples':peoples})

def add_course(request):
    return render(request,"Add Teacher.html")

def add_dept(request):
    pass

def add_teacher(request):
    if request.method == 'POST':
        data = request.POST
        teacher_name = data.get('teacher_name')
        teacher_desig = data.get('teacher_desig')
        subjects = data.get('subjects')
        print(teacher_name, teacher_desig,subjects)
        teacher_data.objects.create(
            teacher_name  = teacher_name,
            teacher_desig = teacher_desig,
            subjects = subjects
        )

    return render(request, "Add Teacher.html")

def index(request):
    pass

def dashboard(request):
    pass

def add_timing(request):
    pass