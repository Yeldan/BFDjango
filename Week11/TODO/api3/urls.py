from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tasks/', views.TaskGenView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailGenView.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register)
]

urlpatterns = format_suffix_patterns(urlpatterns)