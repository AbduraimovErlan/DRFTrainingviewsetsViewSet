from django.shortcuts import render
from ViewSet1.serializers import SerializersBook1
from ViewSet1.models import Book1
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response




class ViewSetBook1(viewsets.ViewSet):
    def list(self, request):
        books = Book1.objects.all()
        serializers = SerializersBook1(books, many=True)
        return Response(serializers.data)



    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book1.objects.get(id=id)
            serializers = SerializersBook1(books)
            return Response(serializers.data)



    def create(self, request):
        serializers = SerializersBook1(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id=pk
        books = Book1.objects.get(pk=id)
        books.delete()
        return Response({"message": "Data delete"})