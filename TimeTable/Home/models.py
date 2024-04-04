from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=30)
    teacher_desig = models.CharField(max_length=20)
    
    def __str__(self):
        return self.teacher_name


class teacher_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length = 35)
    teacher_desig = models.CharField(max_length = 15)
    subjects = models.CharField(max_length = 150)
    

class course_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=25)
    course_c = models.PositiveSmallIntegerField()
    course_subs = models.CharField(max_length=200)

class timing_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timing = models.TimeField(max_length=25)
    timing_class = models.CharField(max_length=30)


class infrastructure_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    infra_name = models.CharField(max_length=25)
    infra = models.CharField(max_length=150)
    infra_value = models.CharField(max_length=25)

class WorkingDays_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Data = models.CharField(max_length = 25)
    Total = models.IntegerField()

