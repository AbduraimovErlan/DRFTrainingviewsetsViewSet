from ViewSet2.models import Book2
from rest_framework import serializers



class SerializersBook2(serializers.ModelSerializer):
    class Meta:
        model = Book2
        fields = '__all__'