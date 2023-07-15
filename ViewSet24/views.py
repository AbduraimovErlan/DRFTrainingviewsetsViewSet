from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet24.models import Book24
from ViewSet24.serializers import SerializersBook24





class ViewSetBook24(viewsets.ViewSet):
    def list(self, request):
        books = Book24.objects.all()
        serializers = SerializersBook24(books, many=True)
        return Response(serializers.data)
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book24.objects.get(id=id)
            serializers = SerializersBook24(books)
            return Response(serializers.data)

    def create(self, request):
        serializers = SerializersBook24(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book24.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})