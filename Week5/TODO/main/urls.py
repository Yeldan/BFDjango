from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.current_tasks),
    path('finished', views.finished_tasks),
    path('ordered', views.ordered_tasks),
    url('task-form', views.TaskCreate.as_view(), name='task-add')
]