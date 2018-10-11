from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import TaskCreate, UserForm
from .models import Task, Owner

def start(request):

    tasks = Task.objects.all()

    context = {'tasks': tasks }

    return render(request, 'todo_list.html', context)

def current_tasks(request):
    
    tasks = Task.objects.filter(mark=True)
    
    context = { 'tasks': tasks }

    return render(request, 'todo_list.html', context)

def finished_tasks(request):
    
    tasks = Task.objects.filter(mark=False)
    
    context = { 'tasks': tasks }
    
    return render(request, 'completed_todo_list.html', context)

def ordered_tasks(request):

    tasks = Task.objects.all().order_by("name")

    context = { 'tasks':tasks }

    return render(request, 'todo_list.html', context)

def add_task(request):
    if request.method == 'POST':
        form = TaskCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start')
    else:
        form = TaskCreate()

    context = { 'form': form }

    return render(request, 'task_form.html', context)

def delete_list(request):

    Task.objects.all().delete()

    return redirect('start')

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('start')

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('start')

        return render(request, self.template_name, {'form': form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('start')
        else:
            error = "username or password incorrect"
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('start')


        