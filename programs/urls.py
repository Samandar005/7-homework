from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.language_list, name='language_list'),
    path('language/create/', views.language_create, name='language_create'),
]
