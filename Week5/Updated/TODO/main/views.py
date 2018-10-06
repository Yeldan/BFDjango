from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskCreate
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