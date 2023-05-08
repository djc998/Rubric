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
    
class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Rubric(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='rubrics')
    question = models.CharField(max_length=255)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.question
