from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404  
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import authenticate, login, logout
import back_end_logic
import time_gen
import email_is_not
from database_data import data_clean_subjects,data_clean_teach,data_clean_course
# Create your views here.

def home(request):
    return render(request, "index.html")#, context={'peoples':peoples})

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email= email).exists():
            messages.error(request,'Incorrect username')
            #return redirect('signup')
        
        user = authenticate(username = email,password = password)
        if user is None:
            messages.error(request,"Invalid password")
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
        
        if email_is_not.email_present(email=email):
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
        else:
            messages.info(request,'Invalid Credentials!!')
            return redirect('signup')

    return render(request, 'signup.html')

@login_required(login_url='login_page')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login_page')
def view_option(request):
    return render(request,'view_options.html')

@login_required(login_url='login_page')
def add_subjects(request):
    if request.method == 'POST':
        data = request.POST
        subject_name = data.get('subject_name')
        Subjects_data.objects.create(
            user = request.user,
            subject_name  = subject_name,
        )
    return render(request,"Add subjects.html")


@login_required(login_url='login_page')
def add_teacher(request):
    if request.method == 'POST':
        data = request.POST
        teacher_name = data.get('teacher_name')
        teacher_desig = data.get('teacher_desig')
        Teacher_data.objects.create(
            user = request.user,
            teacher_name  = teacher_name,
            teacher_desig = teacher_desig,
        )

    return render(request, "Add Teacher.html")

@login_required(login_url='login_page')
def add_courses(request):
    if request.method == 'POST':
        data = request.POST
        course_name = data.get('course_name')
        Course_data.objects.create(
            user = request.user,
            course_name  = course_name,
        )
    return render(request,"Add course.html")


@login_required(login_url='login_page')
def add_teach_subs(request):
    # Convert the list of subjects into a list of tuples
    subjects_data = data_clean_subjects()
    subjects = [(f'ID_{index}', subject) for index, subject in enumerate(subjects_data, start=1)]
    
    # Convert the list of teachers into a list of tuples
    teachers_data = data_clean_teach()
    teachers = [(f'ID_{index}', teacher) for index, teacher in enumerate(teachers_data, start=1)]
    
    selected_teacher = None
    teacher_subjects = None

    if request.method == 'POST':
        teacher_id = request.POST.get('teacher')
        subject_ids = request.POST.getlist('subjects[]')  # Get list of selected subjects

        return render(request, 'schedule_form.html', {
            'teachers': teachers,
            'subjects': subjects,
            'selected_teacher': selected_teacher,
            'teacher_subjects': teacher_subjects
        })
    
    return render(request, 'Add Teach_subs.html',{
        'teachers': teachers,
        'subjects': subjects
    })


@login_required(login_url='login_page')
def add_timing(request):
    if request.method == 'POST':
        data = request.POST
        timing = data.get('timing')
        timing_class = data.get('timing_class')
        Timing_data.objects.create(
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

        Infrastructure_data.objects.create(
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
    time_table_slot,working_hours,working_days, time_table_teach, time_table_labs = back_end_logic.main()
    time_for_lecture = 50
    s_break = 10
    period_range = range(working_hours + 1)
    days = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    lst = time_gen.main(working_hours,start_time,start_min,time_for_lecture,s_break) 
    info = {'list':lst,
            'days':days,
            'working_hours':working_hours,
            'working_days':working_days,
            'time_for_lecture':time_for_lecture,
            'period_range': period_range,
            'time_table_slot':time_table_slot,
            'time_table_teach':time_table_teach,
            'time_table_labs':time_table_labs,
            }
    
    return render(request,'time_table.html',context=info)

@login_required(login_url='login_page')
def time_table_teach(request):
    start_time = 8
    start_min = 50
    working_hours = 4
    working_days = 5
    time_table_slot,working_hours,working_days, time_table_teach, time_table_labs = back_end_logic.main()
    time_for_lecture = 50
    s_break = 10
    period_range = range(working_hours + 1)
    days = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    lst = time_gen.main(working_hours,start_time,start_min,time_for_lecture,s_break) 
    info = {'list':lst,
            'days':days,
            'working_hours':working_hours,
            'working_days':working_days,
            'time_for_lecture':time_for_lecture,
            'period_range': period_range,
            'time_table_slot':time_table_slot,
            'time_table_teach':time_table_teach,
            'time_table_labs':time_table_labs,
            }
    
    return render(request,'time_table_teach.html',context=info)

@login_required(login_url='login_page')
def time_table_lab(request):
    start_time = 8
    start_min = 50
    working_hours = 4
    working_days = 5
    time_table_slot,working_hours,working_days, time_table_teach, time_table_labs = back_end_logic.main()
    time_for_lecture = 50
    s_break = 10
    period_range = range(working_hours + 1)
    days = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    lst = time_gen.main(working_hours,start_time,start_min,time_for_lecture,s_break) 
    info = {'list':lst,
            'days':days,
            'working_hours':working_hours,
            'working_days':working_days,
            'time_for_lecture':time_for_lecture,
            'period_range': period_range,
            'time_table_slot':time_table_slot,
            'time_table_teach':time_table_teach,
            'time_table_labs':time_table_labs,
            }
    
    return render(request,'time_table_lab.html',context=info)