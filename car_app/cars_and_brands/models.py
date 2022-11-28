from django.db import models
from django.contrib.auth.models import AbstractUser


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=200,
        unique=True
    )

    is_active: models.BooleanField(default=True)

    USERNAME_FIELD: 'email'
    REQUIRED_FIELDS = []
