from django.contrib import admin
from django.urls import path, include

from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]