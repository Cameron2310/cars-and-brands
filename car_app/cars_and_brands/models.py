from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Brand(models.Model):
    name = models.CharField(max_length=50)
    img = models.URLField(max_length=250)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="cars")
    price = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=200,
        unique=True
    )
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )
    password = models.CharField(max_length=200)

    USERNAME_FIELD = "uid"

    REQUIRED_FIELDS = ['email', 'password']
