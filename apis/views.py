from rest_framework import generics #Facilidades genericas de django rest framework
from library.models import Books
from .serializers import BooksSerializer #Del serializador interno importo...

# Create your views here.

class BooksAPIView(generics.ListAPIView):
    queryset = Books.objects.all() #Obtengo todos los libros
    serializer_class = BooksSerializer