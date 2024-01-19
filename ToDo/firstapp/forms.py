from django import forms
from .models import ToDoModel

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = ['id', 'target_name', 'target_des']