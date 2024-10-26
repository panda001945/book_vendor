from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Order
from django.contrib.auth.decorators import login_required

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    order, created = Order.objects.get_or_create(user=request.user, book=book, status="Pending")
    order.quantity += 1
    order.total_price = order.quantity * book.price
    order.save()
    return redirect('cart')

@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user, status="Pending")
    return render(request, 'cart.html', {'orders': orders})

from django.views.decorators.http import require_POST
from .forms import UpdateQuantityForm

@require_POST
@login_required
def update_quantity(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user, status="Pending")
    form = UpdateQuantityForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
        order.total_price = order.quantity * order.book.price
        order.save()
    return redirect('cart')
