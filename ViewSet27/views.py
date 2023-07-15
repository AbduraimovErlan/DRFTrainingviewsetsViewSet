from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet27.models import Book27
from ViewSet27.serializers import SerializersBook27



class ViewSetBook27(viewsets.ViewSet):
    def list(self, request):
        books = Book27.objects.all()
        serializers = SerializersBook27(books, many=True)
        return Response(serializers.data)
    def retrieve(self, request, pk):
        id=pk
        if id is not None:
            books = Book27.objects.get(id=id)
            serializers = SerializersBook27(books)
            return Response(serializers.data)
    def create(self, request):
        serializers = SerializersBook27(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id=pk
        books = Book27.objects.get(pk=id)
        books.delete()
        return Response({"message": "Data Deleted"})
