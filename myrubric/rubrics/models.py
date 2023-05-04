from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

class Class(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instructor = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.title