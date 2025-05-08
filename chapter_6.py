
# Chapter 6: Building RESTful APIs with Django REST Framework

# Example of a simple Django REST API using serializers and views
from rest_framework import serializers, viewsets
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    