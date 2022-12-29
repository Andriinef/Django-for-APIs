from rest_framework import generics
from apis.serializers import BookSerializer
from books.models import Book


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
