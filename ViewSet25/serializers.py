from rest_framework import serializers
from ViewSet25.models import Book25




class SerializersBook35(serializers.ModelSerializer):
    class Meta:
        model = Book25
        fields = '__all__'