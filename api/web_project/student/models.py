from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512, null=False)
    dob = models.DateField() 
    address = models.CharField(max_length=256)
    index = models.CharField(max_length=10, unique=True, null=False)
    

class Subject(models.Model):
    name = models.CharField(max_length=128)
    mark = models.PositiveSmallIntegerField(default=5)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)