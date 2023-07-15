from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet29.models import Book29
from ViewSet29.serializers import SerializersBook29



class ViewSetBook29(viewsets.ViewSet):
    def list(self, request):
        books = Book29.objects.all()
        serializers = SerializersBook29(books, many=True)
        return Response(serializers.data)
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book29.objects.get(id=id)
            serializers = SerializersBook29(books)
            return Response(serializers.data)
    def create(self, request):
        serializers = SerializersBook29(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk):
        id=pk
        books = Book29.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})