from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from ViewSet28.models import Book28
from ViewSet28.serializers import SerializersBook28




class ViewSetBook28(viewsets.ViewSet):
    def list(self, reqeust):
        books = Book28.objects.all()
        serializers = SerializersBook28(books, many=True)
        return Response(serializers.data)
    def retrieve(self, reqeust, pk=None):
        id=pk
        if id is not None:
            books = Book28.objects.get(id=id)
            serializers = SerializersBook28(books)
            return Response(serializers.data)

    def create(self, reqeust):
        serializers = SerializersBook28(data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, reqeust, pk):
        id=pk
        books = Book28.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})