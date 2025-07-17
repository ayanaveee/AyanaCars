from django.shortcuts import render
from .models import Car, Category

def index(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'app/detail.html', {'car': car})

def about(request):
    return render(request, 'app/about.html')
