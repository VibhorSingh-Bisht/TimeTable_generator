from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import get_user_model

# Create your views here.

def home(request):
    return render(request, "index.html")#, context={'peoples':peoples})

def login(request):
    return render(request,'login.html')



def signup(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('Teacher_name_s')
        teacher_desig = request.POST.get('Teacher_desig_s')
        email = request.POST.get('email_s')
        password = request.POST.get('password_s')
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('login')
        
        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        
        # Save email and password to the User model
        user.email = email
        user.set_password(password)
        user.save()
        
        # Create a register instance and save additional fields
        register = Register.objects.create(
            user=user,
            teacher_name=teacher_name,
            teacher_desig=teacher_desig
        )
        
        messages.info(request, "User created successfully")
        return redirect('login')

    return render(request, 'signup.html')

def dashboard(request):
    return render(request,'dashboard.html')

def add_course(request):
    if request.method == 'POST':
        data = request.POST
        course_name = data.get('course_name')
        course_c = data.get('course_c')
        course_subs = data.get('subjects')
        print(course_name, course_c,course_subs)
        teacher_data.objects.create(
            course_name  = course_name,
            course_d = course_c,
            course_subs = course_subs
        )
    return render(request,"Add Course.html")

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


def add_timing(request):
    if request.method == 'POST':
        data = request.POST


def add_department(request):
    pass


def time_table(request):
    pass