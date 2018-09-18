from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.current_tasks),
    path('finished', views.finished_tasks)
]