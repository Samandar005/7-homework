from django.shortcuts import render, redirect
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    ctx = {'cars': cars}
    return render(request, 'cars/car-list.html', ctx)

def car_create(request):
    car_name = request.POST.get('car_name')
    model = request.POST.get('model')
    year = request.POST.get('year')
    if car_name and model and year:
        Car.objects.create(
            car_name=car_name,
            model=model,
            year=year
        )
        return redirect('cars:car_list')
    return render(request, 'cars/car-form.html')