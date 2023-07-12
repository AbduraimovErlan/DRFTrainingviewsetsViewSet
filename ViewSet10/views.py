from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ViewSet10.models import Book10
from  ViewSet10.serializers import SerializersBook10





class ViewSetBook10(viewsets.ViewSet):
    def list(self, request):
        books = Book10.objects.all()
        serializers = SerializersBook10(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book10.objects.get(id=id)
            serializers = SerializersBook10(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook10(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book10.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})