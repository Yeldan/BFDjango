from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview, User
from .forms import RestaurantForm, UserForm

def start(request):

    restaurants = Restaurant.objects.all()

    context = { 'restaurants': restaurants }

    return render(request, 'main.html', context)

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start')
        else:
            form = RestaurantForm(request.POST)
            context = { 'form': form }
            return render(request, '/', context)

    else:
        form = RestaurantForm()

    context = { 'form': form }

    return render(request, 'add_res.html', context)

def delete_restaurant(request):

    Restaurant.objects.all().delete()

    return redirect('start')

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, { 'form': form })

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('start')

            user = authentificate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('start')

        return render(request, self.template_name, { 'form': form })

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password = password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('start')
        else:
            error = "username or password is incorrect"
            return render(request, 'login.html', { 'error': error })
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('start')