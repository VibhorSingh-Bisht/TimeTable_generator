from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=30)
    teacher_desig = models.CharField(max_length=20)
    def __str__(self):
        return self.teacher_name


class Teacher_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=35)
    teacher_desig = models.CharField(max_length=20)
    
    
class Subjects_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=70)

class Course_data(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=25)

class Timing_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timing = models.CharField(max_length=15)
    timing_class = models.CharField(max_length=30)


class Infrastructure_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    infra_name = models.CharField(max_length=25)
    infra = models.CharField(max_length=25)
    infra_value = models.CharField(max_length=250)

class WorkingDays_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Data = models.CharField(max_length = 25)
    Total = models.IntegerField()


class TeacherSubjects(models.Model):
    teacher_name = models.CharField(max_length=35)
    teacher_desig = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.teacher_name} teaches {self.subject_name}"
    
class CourseSubjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=25)
    subject_name = models.TextField()  # Store subjects as comma-separated values

    def __str__(self):
        return f"{self.course} - {self.subject_name}"


