from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return f"{self.brand} {self.name}"
