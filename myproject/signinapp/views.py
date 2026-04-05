from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# imp
@api_view(['POST'])
@authentication_classes([])
def signup_view(request):
    serializer = serializers.SignupSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "signup success"})
    return Response(serializer.errors)

@api_view(['POST'])
@authentication_classes([])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response({"msg":"invalid user details"})
    
    login(request, user)
    return Response({
        "msg":"login successfully",
        "username":user.username,
        "email": user.email
        })