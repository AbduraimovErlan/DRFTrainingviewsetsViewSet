from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet22.models import Book22
from ViewSet22.serializers import SerializersBook22




class ViewSetBook22(viewsets.ViewSet):
    def list(self, reqeust):
        books = Book22.objects.all()
        serializers = SerializersBook22(books, many=True)
        return Response(serializers.data)



    def retrieve(self, reqeust, pk=None):
        id=pk
        if id is not None:
            books = Book22.objects.get(id=id)
            serializers = SerializersBook22(books)
            return Response(serializers.data)


    def create(self, reqeust):
        serializers = SerializersBook22(data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, reqeust, pk):
        id=pk
        books = Book22.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})