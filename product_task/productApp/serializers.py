from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name is required")
        return value

    def validate_price(self, value):
        if value<=0:
            raise serializers.ValidationError("Value must be grater than 0")
        return value