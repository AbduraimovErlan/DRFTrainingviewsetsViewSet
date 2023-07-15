from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from ViewSet25.models import Book25
from ViewSet25.serializers import SerializersBook35




class ViewSetBook25(viewsets.ViewSet):
    def list(self, request):
        books = Book25.objects.all()
        serializers = SerializersBook35(books, many=True)
        return Response(serializers.data)
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book25.objects.get(id=id)
            serializers = SerializersBook35(books)
            return Response(serializers.data)

    def create(self, request):
        serializers = SerializersBook35(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book25.objects.get(pk=id)
        books.delete()
        return Response({"message": "Data Delelted"})