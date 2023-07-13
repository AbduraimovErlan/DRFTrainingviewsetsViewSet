from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ViewSet17.models import Book17
from ViewSet17.serializers import SerializersBook17


class ViewSetBook17(viewsets.ViewSet):
    def list(self, request):
        books = Book17.objects.all()
        serializers = SerializersBook17(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book17.objects.get(id=id)
            serializers = SerializersBook17(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook17(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book17.objects.get(pk=id)
        books.delete()
        return Response({"message": "Data Deleted"})

