from .models import User
from rest_framework import serializers
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_emai(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exits")
        return Response({'email':value})
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)