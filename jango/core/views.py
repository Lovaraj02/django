from .serializers import SignupUserSerializers
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response


@api_view(['POST'])
def signup_view(request):
    serializer = SignupUserSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"signup successfully"})
    return Response(serializer.errors)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email, password=password)

    if not user:
        return Response({"msg":"invalid login details"})
    
    return Response({
        'msg':'login successfully..!',
        'username':user.username,
        'email':user.email
    })
