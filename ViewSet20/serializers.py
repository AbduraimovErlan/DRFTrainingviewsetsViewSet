from rest_framework import serializers
from ViewSet20.models import Book20




class SerializesBook20(serializers.ModelSerializer):
    class Meta:
        model = Book20
        fields = '__all__'