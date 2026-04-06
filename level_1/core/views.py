from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response


# profisional
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# when need to do all by func

    # ------------------create/add------------------
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "msg":"Book added successfully",
                "details":serializer.data
            })
        return Response(serializer.errors)
    
    # ------------------update--------------
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "msg":"Updated successfully",
                "data":serializer.data
            })
        return Response(serializer.errors)
    


     # ---------------- PARTIAL UPDATE (PATCH) ----------------
    def partial_update(self, request, *args, **kwargs):

        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data, partial=True)  

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Book partially updated",
                "data": serializer.data
            })

        return Response(serializer.errors)

     # -----------------delete-------------
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Book deleted successfully"
        })

















# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# class CreateAddView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer




# from django.shortcuts import render
# from .serializers import BookSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['POST'])
# def add_book(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"msg":"valid data"})
#     return Response(serializer.errors)
