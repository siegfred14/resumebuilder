from django.db import models
from django.db.models.base import Model

# Create your models here.


class Person(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    highschool = models.CharField(max_length=70)
    degree = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    skill = models.TextField(max_length=1000)
    about_you = models.TextField(max_length=1000)
    previous_work = models.TextField(max_length=1000)
