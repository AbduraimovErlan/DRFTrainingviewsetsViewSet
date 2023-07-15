from rest_framework import serializers
from ViewSet29.models import Book29


class SerializersBook29(serializers.ModelSerializer):
    class Meta:
        model = Book29
        fields = '__all__'