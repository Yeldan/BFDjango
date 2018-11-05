from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post'),
    path('posts/<int:pk>', views.post_detail, name='post_detail')
]