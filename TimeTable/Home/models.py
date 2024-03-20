from django.db import models


# Create your models here.
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