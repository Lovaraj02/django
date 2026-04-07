from .models import User, Product
from rest_framework import serializers
from rest_framework.response import Response

# -------------Signup Serializer---------------
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            print({'email':value})
            raise serializers.ValidationError("Email already exits")
        print({'email':value})
        return value
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


# ---------------- Product serializer -------------------
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("price grater than 0")
        return value