from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     category = self.request.query_params.get('category')
    #     min_price = self.request.query_params.get('min_price')
    #     max_price = self.request.query_params.get('max_price')
    #     stock = self.request.query_params.get('stock')

    #     if category:
    #         queryset = queryset.filter(category__iexact=category)
        
    #     if min_price:
    #         queryset = queryset.filter(price__gte=min_price)
        
    #     if max_price:
    #         queryset = queryset.filter(price__lte=max_price)

    #     if stock is not None:
    #         if stock.lower() == 'true':
    #             queryset = queryset.filter(stock=True)
    #         elif stock.lower() == 'false':
    #             queryset = queryset.filter(stock=False)
        
    #     return queryset