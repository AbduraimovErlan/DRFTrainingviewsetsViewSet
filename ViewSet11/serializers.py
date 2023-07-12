from rest_framework import serializers
from ViewSet11.models import Book11





class SerializersBook11(serializers.ModelSerializer):
    class Meta:
        model = Book11
        fields = "__all__"