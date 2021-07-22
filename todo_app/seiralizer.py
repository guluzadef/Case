from rest_framework import serializers
from .models import Product, Carton


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'width', 'height', 'length')
        read_only_fields = ('id',)


class CartonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carton
        fields = ('id', 'name', 'volume')
        read_only_fields = ('id',)
