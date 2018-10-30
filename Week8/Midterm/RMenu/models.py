from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    number = models.CharField(max_length = 255)
    telephone = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('main')

class Dish(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    price = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)

class Review(models.Model):
    rating = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class DishReview(models.Model):
    dish= models.ForeignKey(Dish, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)