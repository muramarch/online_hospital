from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.base.models import Department

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.IntegerField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)  # Рейтинг доктора
    photo = models.ImageField(null=True, blank=True)  # Фотография доктора

    def __str__(self):
        return self.name
