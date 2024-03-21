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
    path('time_table',time_table,name='time_table'),
    path('login_page',login_page,name='login_page'),
    path('logout',logout,name='logout_page'),
    path('signup',signup,name='signup'),
    path('dashboard',dashboard,name='dashboard'),
]
