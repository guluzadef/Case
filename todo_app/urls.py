from django.urls import path
from .views import *
urlpatterns = [
    path('products/create/',ProductCreate.as_view()),
    path('products/',ProductListApi.as_view()),
    path('box/create/',CartonCreate.as_view()),
    path('boxes',CartonListApi.as_view()),
    path('packages/create/',PackageCreateApi.as_view()),
]
