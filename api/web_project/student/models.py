from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=False)
    dob = models.DateField() 
    address = models.CharField(max_length=256)
    index = models.CharField(max_length=10, unique=True, null=False)
    year = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.index + " " + self.first_name + " " + self.last_name


class Subject(models.Model):
    name = models.CharField(max_length=128)
    mark = models.PositiveSmallIntegerField(default=5)
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name + " " + str(self.mark) + " Student: " + str(self.student)