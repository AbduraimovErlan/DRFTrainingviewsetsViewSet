from ViewSet7.models import Book7
from rest_framework import serializers





class SerializersBook7(serializers.ModelSerializer):
    class Meta:
        model = Book7
        fields = "__all__"
