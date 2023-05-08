from django.contrib import admin

# Register your models here.
from .models import Class, Rubric, Assignment

admin.site.register(Class)
admin.site.register(Assignment)
admin.site.register(Rubric)