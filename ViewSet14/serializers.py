from rest_framework import serializers
from ViewSet14.models import Book14





class SerializersBook14(serializers.ModelSerializer):

    class Meta:
        model = Book14
        fields = '__all__'