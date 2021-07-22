from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    width = models.PositiveIntegerField()  #*
    height = models.PositiveIntegerField() #*
    length = models.PositiveIntegerField() #*

    def __str__(self):
        return f'{self.name}'


class Carton(models.Model):
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
