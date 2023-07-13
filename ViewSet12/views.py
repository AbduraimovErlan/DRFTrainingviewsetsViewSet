from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet12.models import Book12
from ViewSet12.serializers import SerializersBook12




class ViewSetBook12(viewsets.ViewSet):
    def list(self, request):
        books = Book12.objects.all()
        serializers = SerializersBook12(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book12.objects.get(id=id)
            serializers = SerializersBook12(books)
            return Response(serializers.data)

    def create(self, request):
        serializers = SerializersBook12(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book12.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})


