from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    adress=models.IntegerField()
    course=models.CharField(max_length=50)
    passed_by=models.CharField( max_length=50)