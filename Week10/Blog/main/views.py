from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View, TemplateView, ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, PostForm, PostUpdate
from .models import Comment, Post

class StartView(View):

    def get(self, request):

        posts = Post.objects.all()
        
        context = { 'posts': posts }

        return render(request, 'blog.html', context)

class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'author', 'date_published', 'content', 'comment']
    template_name = 'update_post.html'

class PostDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        P = Post.objects.get(pk=pk)
        P.delete()
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