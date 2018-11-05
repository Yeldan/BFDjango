from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View, TemplateView, ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskCreate, UserForm, TaskUpdate
from .models import Task

class StartView(View):

    def get(self, request):

        tasks = Task.objects.all()
        
        context = { 'tasks': tasks }

        return render(request, 'todo_list.html', context)

class CurrentTasksView(LoginRequiredMixin, View):

    def get(self, request):

        tasks = Task.objects.filter(mark=False)
        
        context = { 'tasks': tasks }

        return render(request, 'todo_list.html', context)

class FinishedTasksView(LoginRequiredMixin, View):

    def get(self, request):

        tasks = Task.objects.filter(mark=True)
        
        context = { 'tasks': tasks }

        return render(request, 'completed_todo_list.html', context)

class OrderedTasksView(LoginRequiredMixin, View):

    def get(self, request):

        tasks = Task.objects.all().order_by('name')
        
        context = { 'tasks': tasks }

        return render(request, 'todo_list.html', context)

class TaskAddView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreate
    template_name = 'task_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

# class TaskAddView(View):
    
#     def get(self, request):
#         form = TaskCreate()
#         context = { 'form': form }
#         return render(request, 'task_form.html', context)

#     def post(self, request):
#         form = TaskCreate(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('start')
#         else:
#             form = TaskCreate(request.POST)
#             context = { 'form': form }
#             return render(request, 'start', context)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'created', 'due_on', 'owner', 'mark']
    template_name = 'update_task.html'

# class TaskDeleteView(DeleteView):
#     model = Task

class TaskDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        T = Task.objects.get(pk=pk)
        T.delete()
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