from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ViewSet19.models import Book19
from ViewSet19.serializers import SerializersBook19




class ViewSetBook19(viewsets.ViewSet):
    def list(self, request):
        books = Book19.objects.all()
        serializers = SerializersBook19(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book19.objects.get(id=id)
            serializers = SerializersBook19(books)
            return Response(serializers.data)


    def create(self, reqeust):
        serializers = SerializersBook19(data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book19.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})