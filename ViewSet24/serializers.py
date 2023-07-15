from rest_framework import serializers
from ViewSet24.models import Book24





class SerializersBook24(serializers.ModelSerializer):
    class Meta:
        model = Book24
        fields = '__all__'