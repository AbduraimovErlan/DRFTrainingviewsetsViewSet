from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from ViewSet14.models import Book14
from ViewSet14.serializers import SerializersBook14




class ViewSetBook14(viewsets.ViewSet):
    def list(self, request):
        books = Book14.objects.all()
        serializers = SerializersBook14(books, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        id=pk
        books = Book14.objects.get(id=id)
        serializers = SerializersBook14(books)
        return Response(serializers.data)

    def create(self, reqeust):
        serializers = SerializersBook14(data=reqeust.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, reqeust, pk):
        id=pk
        books = Book14.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})

