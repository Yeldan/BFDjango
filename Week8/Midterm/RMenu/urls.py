from django.urls import path, include
from django.contrib import admin
from . import views
from .views import StartView, AddRestaurantView, RestaurantDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', StartView.as_view(), name='start'),
    path('register', views.UserFormView.as_view(), name="register"),
    path('login', views.log_in, name="login"),
    path('logout', views.logout, name="logout"),
    path('add_res', login_required(AddRestaurantView.as_view()), name="add_res"),
    path('delete/<int:pk>/', login_required(RestaurantDeleteView.as_view())),
]