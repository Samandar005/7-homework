from django.db import models


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
