from django.shortcuts import render
from ViewSet5.models import Book5
from ViewSet5.serializers import SerializersBook5
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



class ViewSetBook5(viewsets.ViewSet):
    def list(self, reqeust):
        books = Book5.objects.all()
        serializers = SerializersBook5(books, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book5.objects.get(id=id)
            serializers = SerializersBook5(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook5(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id=pk
        books = Book5.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})

