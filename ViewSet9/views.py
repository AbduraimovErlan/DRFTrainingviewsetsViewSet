from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet9.serializers import SerializersBook9
from ViewSet9.models import Book9




class ViewSetBook9(viewsets.ViewSet):
    def list(self, request):
        books = Book9.objects.all()
        serializers = SerializersBook9(books, many=True)
        return Response(serializers.data)



    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book9.objects.get(id=id)
            serializers = SerializersBook9(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook9(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book9.objects.get(pk=id)
        books.delete()
        return Response({"message": "Data Deleted"})