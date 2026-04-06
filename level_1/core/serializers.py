from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("title cannot be empty")
        return value
    
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("price must be grater than 0")
        return value
    

    