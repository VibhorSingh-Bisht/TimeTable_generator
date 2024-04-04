from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import authenticate, login, logout
from back_end_logic import *
from time_gen import main

# Create your views here.

def home(request):
    return render(request, "index.html")#, context={'peoples':peoples})

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email= email).exists():
            messages.error(request,'Invalid password')
            return redirect('signup')
        
        user = authenticate(username = email,password = password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('login_page')
        else:
            login(request,user)
            return redirect('dashboard')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def signup(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_desig = request.POST.get('teacher_desig')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('login_page')
        
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
        return redirect('login_page')

    return render(request, 'signup.html')

@login_required(login_url='login_page')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login_page')
def add_course(request):
    if request.method == 'POST':
        data = request.POST
        course_name = data.get('course_name')
        course_c = data.get('course_c')
        course_subs = data.get('course_subs')
        print(course_name, course_c,course_subs)
        course_data.objects.create(
            user = request.user,
            course_name  = course_name,
            course_c = course_c,
            course_subs = course_subs
        )
    return render(request,"Add Course.html")


@login_required(login_url='login_page')
def add_teacher(request):
    if request.method == 'POST':
        data = request.POST
        teacher_name = data.get('teacher_name')
        teacher_desig = data.get('teacher_desig')
        subjects = data.get('subjects')
        teacher_data.objects.create(
            user = request.user,
            teacher_name  = teacher_name,
            teacher_desig = teacher_desig,
            subjects = subjects
        )

    return render(request, "Add Teacher.html")

@login_required(login_url='login_page')
def add_timing(request):
    if request.method == 'POST':
        data = request.POST
        timing = data.get('timing')
        timing_class = data.get('timing_class')
        timing_data.objects.create(
            user = request.user,
            timing  = timing,
            timing_class = timing_class
        )
    return render(request,'Add Timing.html')

@login_required(login_url='login_page')
def add_infrastructure(request):
    if request.method == 'POST':
        data = request.POST
        infra_name = data.get('infra_name')
        infra = data.get('infra')
        infra_value = data.get('infra_value')

        infrastructure_data.objects.create(
            user = request.user,
            infra_name = infra_name,
            infra = infra,
            infra_value = infra_value
        )
    return render(request,'Add Infrastructure.html')

@login_required(login_url='login_page')
def add_working_days(request):
    if request.method == 'POST':
        data = request.POST
        Total = data.get('Total')
        Data = data.get('Data')
        WorkingDays_data.objects.create(
            user = request.user,
            Total  = Total,
            Data = Data
        )
    return render(request,'Add Working_days.html')


@login_required(login_url='login_page')
def time_table(request):
    start_time = 8
    start_min = 50
    working_hours = 4
    working_days = 5
    time_for_lecture = 50
    s_break = 10
    period_range = range(working_hours + 1)
    days = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    lst = main(working_hours,start_time,start_min,time_for_lecture,s_break)
    info = {'list':lst,
            'days':days,
            'working_hours':working_hours,
            'working_days':working_days,
            'time_for_lecture':time_for_lecture,
            'period_range': period_range
            }
    
    return render(request,'time_table.html',context=info)