from django.contrib import admin
from .models import Comment, Post

class CustomComment(admin.ModelAdmin):
    list_display = ('id', 'comments', 'left_by')
    list_display_links = ('id', 'comments', 'left_by')
    search_fields = ('id', 'comments', 'left_by')
    list_per_page = 10

class CustomPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'date_published', 'content', 'comment')
    list_display_links = ('id', 'title', 'author', 'date_published', 'content', 'comment')
    search_fields = ('id', 'title', 'author', 'date_published', 'content')
    list_per_page = 5

admin.site.register(Comment, CustomComment)
admin.site.register(Post, CustomPost)
