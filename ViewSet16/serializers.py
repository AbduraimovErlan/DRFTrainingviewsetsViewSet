from rest_framework import serializers
from ViewSet16.models import Book16




class SerializesBook16(serializers.ModelSerializer):
    class Meta:
        model = Book16
        fields = "__all__"