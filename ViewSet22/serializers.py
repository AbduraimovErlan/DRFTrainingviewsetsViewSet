from rest_framework import serializers
from ViewSet22.models import Book22




class SerializersBook22(serializers.ModelSerializer):
    class Meta:
        model = Book22
        fields = '__all__'