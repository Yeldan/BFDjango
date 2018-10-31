from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    comments = models.CharField(max_length = 255)
    left_by = models.CharField(max_length = 255)

    def __str__(self):
        return self.left_by + ": " + self.comments

class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(author=user)

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_published = models.CharField(max_length = 255)
    content = models.CharField(max_length = 1000)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('start')