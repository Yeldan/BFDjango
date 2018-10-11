from django.forms import ModelForm
from main.models import Comment, Post
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 
 
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'date_published', 'content', 'comment')