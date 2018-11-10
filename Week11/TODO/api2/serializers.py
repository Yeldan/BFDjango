from rest_framework import serializers
from main.models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    created = serializers.CharField(max_length=255)
    due_on = serializers.CharField(max_length=255)
    owner = UserSerializer(read_only=True)
    mark = serializers.BooleanField()
    
    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.due_on = validated_data.get('due_on', instance.due_on)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.mark = validated_data.get('mark', instance.mark)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'created', 'due_on', 'owner', 'mark']