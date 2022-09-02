from platform import mac_ver
from django.db import models
# from __future__ import unicode_literals

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=75)
    age = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class Meta:
        db_table = 'student'

class Employees(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = "employees"