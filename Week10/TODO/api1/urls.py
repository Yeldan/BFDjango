from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/<int:pk>', views.task_detail, name='task_detail'),
]