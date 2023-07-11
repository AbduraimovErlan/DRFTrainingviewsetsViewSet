from django.shortcuts import render
from ViewSet6.models import Book6
from ViewSet6.serializers import SerializersBook6
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets




class ViewSetBook6(viewsets.ViewSet):
    def list(self, request):
        books = Book6.objects.all()
        serializers = SerializersBook6(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book6.objects.get(id=id)
            serializers = SerializersBook6(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook6(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book6.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})

