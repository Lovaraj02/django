from django.contrib.auth.models import User
from rest_framework import serializers

class SignupSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        # fields = '__all__'

    def validate_email(self, value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError("email already exists")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
