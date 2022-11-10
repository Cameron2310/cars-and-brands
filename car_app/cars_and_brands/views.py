from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Views for Brands
def home(request):
    data = Brand.objects.order_by('name')

    brand = {'brand': data}
    return render(request, 'home.html', brand)


def new(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            brand = Brand()
            brand.name = request.POST.get('name')
            brand.save()

    return render(request, 'new.html')


def brand_details(request, id):
    brand = Brand.objects.get(id=id)
    return render(request, 'brand_details.html', {'brand': brand.__dict__})


def edit(request, id):
    brand = Brand.objects.get(id=id)
    return render(request, 'edit.html', {'brand': brand.__dict__})


def update_record(request, id):
    name = request.POST.get('name')
    brand = Brand.objects.get(id=id)
    brand.name = name
    brand.save()

    return HttpResponseRedirect(reverse('home'))


def cars(request, brand_id):
    data = Car.objects.filter(brand=brand_id)

    car = {'car': data, 'brand_id': brand_id}
    return render(request, 'cars.html', car)


def new_car(request, brand_id):
    if request.method == 'POST':
        if request.POST.get('name'):
            car = Car()
            car.name = request.POST.get('name')
            car.brand = Brand.objects.get(id=brand_id)
            car.save()

    return render(request, 'new_car.html', {'brand_id': brand_id})


def car_details(request, brand_id, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_details.html', {'car': car.__dict__, 'brand_id': brand_id})


def edit_car(request, brand_id, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'edit_car.html', {'car': car.__dict__, 'brand_id': brand_id})


def update_car_record(request, brand_id, car_id):
    name = request.POST.get('name')
    car = Car.objects.get(id=car_id)
    car.name = name
    car.save()

    return HttpResponseRedirect(reverse('home'))
