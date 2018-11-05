from rest_framework import serializers
from main.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = UserSerializer(read_only=True)
    date_published = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    comment = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.date_published = validated_data.get('date_published', instance.date_published)
        instance.content = validated_data.get('content', instance.content)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'author', 'date_published', 'content', 'comment']