from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    width = models.PositiveIntegerField()  # *
    height = models.PositiveIntegerField()  # *
    length = models.PositiveIntegerField()  # *

    def __str__(self):
        return f'{self.name}'

    def get_volume(self):
        return self.width * self.height * self.length


class Carton(models.Model):
    name = models.CharField(max_length=255)
    volume = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name='products', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Packages(models.Model):
    products = models.ManyToManyField(Product, null=True, blank=True)
    carton = models.ForeignKey(Carton, null=True, blank=True,on_delete=models.CASCADE)
