from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewsets(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class  = serializers.BooksSerializers
