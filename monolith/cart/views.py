from django.shortcuts import redirect, render
from .models import Cart, CartItem
from books.models import Book
from accounts.models import Customer

def add_to_cart(request, book_id):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')

    customer = Customer.objects.get(id=customer_id)
    cart, _ = Cart.objects.get_or_create(customer=customer)

    book = Book.objects.get(id=book_id)
    item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not created:
        item.quantity += 1
    else:
        item.quantity = 1

    item.save()
    return redirect('book_list')


def view_cart(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('login')

    customer = Customer.objects.get(id=customer_id)
    cart = Cart.objects.filter(customer=customer).first()

    items = cart.cartitem_set.all() if cart else []

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'items': items
    })

