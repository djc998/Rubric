from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'instructor']
        labels = {'name': 'Class Name', 'instructor': 'Instructor Name'}
        widgets = {'name': forms.TextInput(attrs={'size': 20})}
