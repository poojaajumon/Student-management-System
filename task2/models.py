from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    place=models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
