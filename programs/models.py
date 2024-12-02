from django.db import models


class Program(models.Model):
    language_name = models.CharField(max_length=100)
    description = models.TextField()