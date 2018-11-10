from django.forms import ModelForm
from main.models import Task
from django.contrib.auth.models import User
from django import forms

class TaskCreate(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'created', 'due_on', 'owner', 'mark']

class TaskUpdate(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'created', 'due_on', 'owner', 'mark']

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 