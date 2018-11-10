from rest_framework import serializers
from main.models import Post
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class PostModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'author', 'date_published', 'content', 'comment']
