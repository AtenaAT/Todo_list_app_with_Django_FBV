from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": " new task..."}))

    class Meta:
        model = Task
        fields = 'title', 'user'