from rest_framework import generics, viewsets
from relationshipapp.models import Librarian, Library, Book
from .serializers import BooksSerializer, LibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    


