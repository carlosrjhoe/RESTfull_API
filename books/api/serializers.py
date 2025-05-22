from rest_framework import serializers
from books import models


class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'
