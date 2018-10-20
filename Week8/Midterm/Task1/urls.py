from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('register', views.UserFormView.as_view(), name="register"),
    path('login', views.log_in, name="login"),
    path('logout', views.logout, name="logout"),
    path('add_res', views.add_restaurant, name="add_res")
]