from rest_framework import serializers
from ViewSet23.models import Book23



class SerializersBook23(serializers.ModelSerializer):
    class Meta:
        model = Book23
        fields = "__all__"