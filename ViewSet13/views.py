from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from ViewSet13.models import Book13
from ViewSet13.serializers import SerializersBook13



class ViewSetBook13(viewsets.ViewSet):
    def list(self, request):
        books = Book13.objects.all()
        serializers = SerializersBook13(books, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book13.objects.get(id=id)
            serializers = SerializersBook13(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook13(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, pk):
        id=pk
        books = Book13.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})