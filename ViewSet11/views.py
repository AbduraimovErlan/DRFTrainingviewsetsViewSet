from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from ViewSet11.models import Book11
from ViewSet11.serializers import SerializersBook11




class ViewSetBook11(viewsets.ViewSet):
    def list(self, request):
        books = Book11.objects.all()
        serializers = SerializersBook11(books, many=True)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            books = Book11.objects.get(id=id)
            serializers = SerializersBook11(books)
            return Response(serializers.data)


    def create(self, request):
        serializers = SerializersBook11(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk):
        id=pk
        books = Book11.objects.get(pk=id)
        books.delete()
        return Response({'message': 'Data Delete'})