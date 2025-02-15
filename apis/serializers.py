from rest_framework import serializers
from library.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__' #Campos que quiero serializar (en este caso todos los del modelo )