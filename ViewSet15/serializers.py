from rest_framework import serializers
from ViewSet15.models import Book15



class SerializersBook15(serializers.ModelSerializer):
    class Meta:
        model = Book15
        fields = '__all__'