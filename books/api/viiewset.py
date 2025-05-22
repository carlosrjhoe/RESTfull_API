from rest_framework import viewsets
from books.api import serializers
from books import models


class BooksViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializers
    queryset = models.Books.objects.all()
