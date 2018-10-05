from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task, Owner

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

    context = {'tasks':tasks }

    return render(request,'todo_list.html',context)

class TaskCreate(CreateView):
    model = Task
    fields = ['name', 'created', 'due_on', 'owner'] 