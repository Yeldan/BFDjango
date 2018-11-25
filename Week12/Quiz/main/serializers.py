from rest_framework import serializers
from .models import Advert
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class AdvertModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ['title', 'address', 'description', 'price', 'number_of_views', 'owner']
