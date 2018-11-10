from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StartView.as_view(), name='start'),
    path('register', views.UserFormView.as_view(), name="register"),
    path('login', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('create', views.PostAddView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete')
]