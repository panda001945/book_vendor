from rest_framework import serializers
from .models import Book, Order

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'price', 'stock', 'description']

class OrderSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'quantity', 'total_price', 'status', 'created_at']
