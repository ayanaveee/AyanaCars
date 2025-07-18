from django.shortcuts import render, redirect
from .models import Car, Category

def index(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'app/detail.html', {'car': car})

def about(request):
    return render(request, 'app/about.html')

from django.shortcuts import render, redirect
from .models import Car, Category

def car_announcement(request):
    if request.method == "POST":
        title = request.POST['title']
        model = request.POST['model']
        category_id = request.POST['category']
        engine_volume = request.POST['engine_volume']
        color = request.POST['color']
        transmission = request.POST['transmission']
        price = request.POST['price']
        year_of_manufacture = request.POST['year_of_manufacture']
        location = request.POST['location']
        registration = request.POST['registration']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        car = Car(
            title=title,model=model,engine_volume=engine_volume,color=color,transmission=transmission,price=price, year_of_manufacture=year_of_manufacture,location=location,registration=registration,image=image,category=category)
        car.save()

        return redirect('index')

    categories = Category.objects.all()
    return render(request, 'app/car_announcement.html', {'categories': categories})


