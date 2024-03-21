from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class login_register(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True)
    email_l = models.EmailField()
    password_l = models.CharField(max_length = 20)


class teacher_data(models.Model):
    teacher_name = models.CharField(max_length = 35)
    teacher_desig = models.CharField(max_length = 15)
    subjects = models.CharField(max_length = 150)
    

class course_data(models.Model):
    course_name = models.CharField(max_length=25)
    course_c = models.PositiveSmallIntegerField()
    course_subs = models.CharField(max_length=200)

class timing_data(models.Model):
    course_name = models.CharField(max_length=25)
    course_c = models.PositiveSmallIntegerField()
    course_subs = models.CharField(max_length=200)


class department_data(models.Model):
    course_name = models.CharField(max_length=25)
    course_c = models.PositiveSmallIntegerField()
    course_subs = models.CharField(max_length=200)