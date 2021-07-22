from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import Product, Carton, Packages

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView
from .seiralizer import ProductSerializer, CartonSerializer, TaskSerializer


# Create your views here.

class ProductCreate(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        user_data = super().create(request, *args, **kwargs).data
        product = Product.objects.get(pk=user_data['id'])
        data = {
            'name': product.name,

        }

        return Response(data, status=status.HTTP_201_CREATED)


class ProductListApi(APIView):  # GET all persons
    permission_classes = (AllowAny,)

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class CartonCreate(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CartonSerializer

    def create(self, request, *args, **kwargs):
        user_data = super().create(request, *args, **kwargs).data
        carton = Carton.objects.get(pk=user_data['id'])
        data = {
            'name': carton.name,

        }

        return Response(data, status=status.HTTP_201_CREATED)


class CartonListApi(APIView):  # GET all persons
    permission_classes = (AllowAny,)

    def get(self, request):
        carton = Carton.objects.all()
        serializer = CartonSerializer(carton, many=True)
        return Response(serializer.data)


class PackageCreateApi(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        task_data = super().create(request, *args, **kwargs).data
        product = task_data.get('products')
        task = Packages.objects.get(pk=task_data['id'])
        count = 0
        for e in product:
            a = Product.objects.filter(id=e).last()
            count += a.get_volume()
        try:
            carton = Carton.objects.filter(volume__gte=count).order_by('volume').first()
            task.carton_id = carton.id
            task.save()
            data = {
                'id': task.id
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            return Response({
                "message": "This User Already Exists "
            }, status=status.HTTP_404_NOT_FOUND)
