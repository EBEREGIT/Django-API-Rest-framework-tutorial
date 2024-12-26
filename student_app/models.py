from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    owner = models.ForeignKey(User, related_name="students", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    about = models.TextField()
