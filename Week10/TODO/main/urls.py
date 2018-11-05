from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),
    path('register', views.UserFormView.as_view(), name='register'),
    path('login', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('current', views.CurrentTasksView.as_view()),
    path('finished', views.FinishedTasksView.as_view()),
    path('ordered', views.OrderedTasksView.as_view()),
    path('add_task', views.TaskAddView.as_view(), name='add_task'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete')
]