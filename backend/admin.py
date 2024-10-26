from django.contrib import admin
from .models import Book, Order

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price', 'stock')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'quantity', 'total_price', 'status', 'created_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('status', 'created_at')
