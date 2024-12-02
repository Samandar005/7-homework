from django.urls import path
from . import views


app_name = 'cars'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('cars/create/', views.car_create, name='car_create'),
]
