from rest_framework import serializers
from relationshipapp.models import Librarian, Library, Book

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="book-detail",
        read_only=True
    )

    class Meta:
        model = Library
        fields = ['url', 'name', 'books']


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name="author-detail",
        read_only=True
    )

    class Meta:
        model = Book
        fields = ['url', 'title', 'publication_year', 'author']
