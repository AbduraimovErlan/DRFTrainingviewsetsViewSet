from django.shortcuts import render
from ViewSet2.serializers import SerializersBook2
from ViewSet2.models import Book2
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets



class ViewSetBook2(viewsets.ViewSet):
    def list(self, request):
        books = Book2.objects.all()
        serializers = SerializersBook2(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book2.objects.get(id=id)
            serializers = SerializersBook2(books)
            return Response(serializers.data)



    def create(self, request):
        serializers = SerializersBook2(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id=pk
        books = Book2.objects.get(id=id)
        books.delete()
        return Response({"message": "Data deleted"})

