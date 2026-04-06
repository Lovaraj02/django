from django.shortcuts import render
from .serializers import ProductSerializers
from rest_framework.viewsets import ModelViewSet
from .models import Product

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category')
        price = self.request.query_params.get('price')

        if category:
            queryset = queryset.filter(category__icontains=category)

        if price:
            queryset = queryset.filter(price__gte=1000)

        return queryset




