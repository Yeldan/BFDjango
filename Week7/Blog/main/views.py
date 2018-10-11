from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm, PostForm
from .models import Comment, Post

def start(request):

    posts = Post.objects.all()

    context = { 'posts': posts }

    return render(request, 'blog.html', context)

def view_blog(request):
    
    posts = Post.objects.all()
    
    context = { 'posts': posts }

    return render(request, 'blog.html', context)

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

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start')
    else:
        form = PostForm()
        
    context = { 'form': form }

    return render(request, 'create_post.html', context)