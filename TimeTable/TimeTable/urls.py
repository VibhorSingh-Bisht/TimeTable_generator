"""
URL configuration for TimeTable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('add_teacher',add_teacher,name='add_teacher'),
    path('add_timing',add_timing,name='add_timing'),
    path('add_subjects',add_subjects,name='add_subjects'),
    path('add_courses',add_courses,name='add_courses'),
    path('add_teach_subs',add_teach_subs,name='add_teach_subs'),
    path("add_course_subs",add_course_subs,name='add_course_subs'),
    path('add_infrastructure',add_infrastructure,name='add_infrastructure'),
    path('add_working',add_working_days,name='add_working_days'),
    path('time_table',time_table,name='time_table'),
    path('time_table_teach',time_table_teach,name='time_table_teach'),
    path('time_table_lab',time_table_lab,name='time_table_lab'),
    path('login_page',login_page,name='login_page'),
    path('logout',logout,name='logout_page'),
    path('signup',signup,name='signup'),
    path('dashboard',dashboard,name='dashboard'),
    path('view_options',view_option,name='view_options')
]
