from django.shortcuts import render
from .models import Comment, Post

def view_blog(request):
    
    posts = Post.objects.all()
    
    context = { 'posts': posts }

    return render(request, 'blog.html', context)

