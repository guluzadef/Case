from rest_framework import serializers
from .models import Product, Carton, Packages


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'width', 'height', 'length')
        read_only_fields = ('id',)


class CartonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carton
        fields = ('id', 'name', 'volume', 'products')
        read_only_fields = ('id',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ('id', 'products',
                  )
        read_only_fields = ('id',)
