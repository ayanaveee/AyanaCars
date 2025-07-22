from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Car, Category
from .forms import CarForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'app/detail.html', {'car': car})

def about(request):
    return render(request, 'app/about.html')

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

def car_update(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        car.title = request.POST['title']
        car.model = request.POST['model']
        car.category_id = request.POST['category']
        car.engine_volume = request.POST['engine_volume']
        car.color = request.POST['color']
        car.transmission = request.POST['transmission']
        car.price = request.POST['price']
        car.year_of_manufacture = request.POST['year_of_manufacture']
        car.location = request.POST['location']
        car.registration = request.POST['registration']
        car.image = request.FILES['image']

        car.save()
        return redirect('car_detail', car_id=car.id)
    categories = Category.objects.all()
    return render(request, 'app/car_data_update.html', {'car': car, 'categories': categories})


def delete_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('index')
    return render(request, 'app/car_delete.html', {'car': car})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CarForm

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'app/car_form.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно создали аккаунт!')
            return redirect('index')

        for field, errors in form.errors.items():

            for error in errors:
                messages.error(request, f'{error}')

    form = UserCreationForm()

    return render(request=request, template_name='app/user_register.html', context={"form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('index')

        messages.error(request, 'Неправильный логин или пароль')

    return render(request, 'app/user_login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('index')