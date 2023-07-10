from ViewSet3.models import Book3
from rest_framework import serializers



class SerializesBook3(serializers.ModelSerializer):
    class Meta:
        model = Book3
        fields = '__all__'