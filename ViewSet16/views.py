from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet16.models import Book16
from ViewSet16.serializers import SerializesBook16



class ViewSetBook16(viewsets.ViewSet):
    def list(self, request):
        books = Book16.objects.all()
        serializers = SerializesBook16(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book16.objects.get(id=id)
            serializers = SerializesBook16(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializesBook16(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book16.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})

