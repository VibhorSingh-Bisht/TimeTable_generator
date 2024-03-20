from django.db import models


# Create your models here.
class teacher_data(models.Model):
    teacher_name = models.CharField(max_length = 35)
    teacher_desig = models.CharField(max_length = 15)
    subjects = models.CharField(max_length = 150)
    


