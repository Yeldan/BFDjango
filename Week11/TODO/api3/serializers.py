from rest_framework import serializers
from main.models import Task
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class TaskModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['name', 'created', 'due_on', 'owner', 'mark']