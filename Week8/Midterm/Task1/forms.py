from django.forms import ModelForm
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview, User
from django.contrib.auth.models import User
from django import forms

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'number', 'telephone', 'city', 'user']

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']