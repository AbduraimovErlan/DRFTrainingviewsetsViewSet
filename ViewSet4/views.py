from django.shortcuts import render
from ViewSet4.models import Book4
from ViewSet4.serializers import SerializersBook4
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets




class ViewSetBook4(viewsets.ViewSet):
    def list(self, request):
        books = Book4.objects.all()
        serializers = SerializersBook4(books, many=True)
        return Response(serializers.data)

    def retrieve(self, reqeust, pk=None):
        id=pk
        if id is not None:
            books = Book4.objects.get(id=id)
            serializers = SerializersBook4(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook4(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'massage': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book4.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})



