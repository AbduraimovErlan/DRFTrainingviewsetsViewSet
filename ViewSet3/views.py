from django.shortcuts import render
from ViewSet3.models import Book3
from ViewSet3.serializers import SerializesBook3
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status





class ViewSetBook3(viewsets.ViewSet):
    def list(self, request):
        books = Book3.objects.all()
        serializers = SerializesBook3(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book3.objects.get(id=id)
            serializes = SerializesBook3(books)
            return Response(serializes.data)


    def create(self, request):
        serializers = SerializesBook3(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'massage': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book3.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})
