from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from ViewSet20.models import Book20
from ViewSet20.serializers import SerializesBook20




class ViewSetBook20(viewsets.ViewSet):
    def list(self, request):
        books = Book20.objects.all()
        serializes = SerializesBook20(books, many=True)
        return Response(serializes.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book20.objects.get(id=id)
            serializers = SerializesBook20(books)
            return Response(serializers.data)


    def create(self, request):
        serializes = SerializesBook20(data=request.data)
        if serializes.is_valid():
            serializes.save()
            return Response({"message": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializes.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book20.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Deleted'})


