from rest_framework import serializers
from ViewSet28.models import Book28




class SerializersBook28(serializers.ModelSerializer):
    class Meta:
        model = Book28
        fields = '__all__'