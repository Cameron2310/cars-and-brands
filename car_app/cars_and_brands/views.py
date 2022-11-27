from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import *
from .models import *


# Views for Brands

class Home(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarAPIView(APIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        cars = Car.objects.all()
        return cars

    def get(self, request):
        id = request.query_params["id"]
        if id != None:
            cars = Car.objects.filter(brand=id)
            serializer = CarSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        try:
            car_brand = Brand.objects.get(name=data['brand.name'])
            new_car = Car.objects.create(name=data['name'], brand=car_brand)

        except:
            new_brand = Brand.objects.create(name=data['brand.name'])
            new_brand.save()

            new_car = Car.objects.create(name=data['name'], brand=new_brand)

        new_car.save()

        serializer = CarSerializer(new_car)

        return Response(serializer.data)


class FilterBrandAPIView(APIView):
    serializer_class = BrandSerializer

    def get(self, request, name=None):
        if name != None:
            brand = Brand.objects.get(name=name)
            serializer = BrandSerializer(brand)

            return Response(serializer.data)

        else:
            brands = Brand.objects.all()
            serializer = BrandSerializer(brands, many=True)
            return Response(serializer.data)
