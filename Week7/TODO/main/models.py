from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length = 255)
    created = models.CharField(max_length = 255)
    due_on = models.CharField(max_length = 255)
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    mark = models.BooleanField(default = True)