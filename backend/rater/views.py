from django.shortcuts import render
from .models import Product, Rating, Category
from .serializers import ProductSerializer, RatingSerializer, CategorySerializer
from rest_framework import viewsets




# 1 - Endpoint - list of products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(active=True)
    serializer_class = ProductSerializer




# 2 - Endpoint - list of Rating 
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer




class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer