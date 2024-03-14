from django.shortcuts import render

# Create your views here.

def home(request):
    """peoples = [
        {"Name":"Vibhor Singh","age":21},
        {"Name":"Abhijeet","age":22},
        {"Name":"ACP Parduman","age":21},
        {"Name":"Daya","age":21}
    ]"""
    return render(request, "Add Teacher.html")#, context={'peoples':peoples})

def add_course(request):
    return render(request,"Add Teacher.html")

def add_dept(request):
    pass

def add_teacher(request):
    if request.method == 'POST':
        data = request.POST
        teacher_name = data.get('teacher_name')
    return render(request, "Add Teacher.html")

def index(request):
    pass

def dashboard(request):
    pass

def add_timing(request):
    pass