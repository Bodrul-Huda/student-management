from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  
    phone = models.CharField(max_length=15)  
    course = models.CharField(max_length=50, choices=COURSE_CHOICES) 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

