from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book, Order

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Sample Book",
            author="Author Name",
            genre="Fiction",
            price=20.00,
            stock=10,
            description="A sample book description."
        )

    def test_book_str(self):
        book = Book.objects.get(title="Sample Book")
        self.assertEqual(str(book), "Sample Book")

class OrderModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        book = Book.objects.create(
            title="Sample Book",
            author="Author Name",
            genre="Fiction",
            price=20.00,
            stock=10
        )
        Order.objects.create(user=user, book=book, quantity=2, total_price=40.00)

    def test_order_creation(self):
        order = Order.objects.get(quantity=2)
        self.assertEqual(order.total_price, 40.00)
