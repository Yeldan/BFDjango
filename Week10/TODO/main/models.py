from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your models here.

class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class Task(models.Model):
    name = models.CharField(max_length = 255)
    created = models.CharField(max_length = 255)
    due_on = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    objects = TaskManager()
    mark = models.BooleanField()

    def get_absolute_url(self):
        return reverse_lazy('start')

    def to_json(self):
        return {
            'name': self.name,
            'created': self.created,
            'due_on': self.due_on,
            'owner': self.owner,
            'mark': self.mark
        }