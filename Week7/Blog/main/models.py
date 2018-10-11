from django.db import models

# Create your models here.


class Comment(models.Model):
    comments = models.CharField(max_length = 255)
    left_by = models.CharField(max_length = 255)

    def __str__(self):
        return self.left_by + ": " + self.comments

class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    date_published = models.CharField(max_length = 255)
    content = models.CharField(max_length = 255)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)