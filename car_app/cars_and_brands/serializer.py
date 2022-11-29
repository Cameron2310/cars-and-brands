from rest_framework import serializers
from .models import *


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ["id", "name", "img"]


class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand', 'price']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
