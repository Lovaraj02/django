from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Product

# --------------signup-----------------------
class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer)
            return Response({'msg':'User Registered successfully', 'details':serializer.data})
        return Response(serializer.errors)

# ---------------display login user details---------------
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
    

# ----------------Product view-----------------
class ProductModelViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    # ----------params--------------
    def get_queryset(self):
        queryset = super().get_queryset()

        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    
