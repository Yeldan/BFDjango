from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.view_blog),
    path('', views.start, name='start'),
    path('register', views.UserFormView.as_view(), name="register"),
    path('login', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('create', views.create_post , name='create')
]