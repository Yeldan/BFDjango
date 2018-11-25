from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('adverts/', views.AdvertView.as_view()),
    path('adverts/<int:pk>', views.AdvertDetails.as_view()),
    #path('adverts/', views.AdvertCBV.as_view()),
    #path('adverts/<int:pk>', views.AdvertDetailCBV.as_view()),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout)
]

urlpatterns = format_suffix_patterns(urlpatterns)