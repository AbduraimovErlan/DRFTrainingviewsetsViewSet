from rest_framework import serializers
from ViewSet27.models import Book27



class SerializersBook27(serializers.ModelSerializer):
    class Meta:
        model = Book27
        fields = '__all__'