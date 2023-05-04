from django.contrib import admin

# Register your models here.
from .models import Class, Book

admin.site.register(Class)
admin.site.register(Book)