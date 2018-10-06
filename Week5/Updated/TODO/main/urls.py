from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.current_tasks),
    path('', views.start, name='start'),
    path('finished', views.finished_tasks),
    path('ordered', views.ordered_tasks),
    path('add_task', views.add_task, name="add_task"),
    path('delete_list', views.delete_list, name="delete_list")
]