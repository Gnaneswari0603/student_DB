from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    mobile=models.IntegerField()
    course=models.CharField(max_length=100)
