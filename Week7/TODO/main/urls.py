from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.current_tasks),
    path('register', views.UserFormView.as_view(), name="register"),
    path('login', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.start, name='start'),
    path('finished', views.finished_tasks),
    path('ordered', views.ordered_tasks),
    path('add_task', views.add_task, name="add_task"),
    path('delete_list', views.delete_list, name="delete_list")
]