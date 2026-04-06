from rest_framework import serializers
from .models import SignupUser

class SignupUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = SignupUser
        fields = ['username', 'email', 'password']

    def validate_email(self,value):
        if SignupUser.objects.filter(email = value).exists():
            raise serializers.ValidationError("email already exits")
        return value
    
    def create(self,validated_data):
        return SignupUser.objects.create_user(**validated_data)


# another way to create user
# def create(self, validated_data):
# username = validated_data.get('username')
# email = validated_data.get('email')
# password = validated_data.get('password')

# return SignupUser.objects.create_user(
#     username=username,
#     email=email,
#     password=password
    # )    
