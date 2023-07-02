from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
    order, created = Order.objects.get_or_create(user=request.user)
    order_items = order.orderitem_set.all()
    order.update_total_amount()  # Update the total_amount field
    total_amount = order.total_amount
    if order_items.count() == 0:
        return redirect('product_list')
    return render(request, 'cart/cart.html', {'order_items': order_items, 'total_amount': total_amount})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user)
    order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += int(request.POST.get('quantity', 1))
    order_item.save()
    return redirect('cart')

def remove_from_cart(request, order_item_id):
    item = get_object_or_404(OrderItem, id=order_item_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity >= item.quantity:
        item.delete()
    else:
        item.quantity -= quantity
        item.save()
    if item.quantity == 0:
        return redirect('product_list')
    return redirect('cart')

def clear_cart(request):
    order = Order.objects.get(user=request.user)
    order.orderitem_set.all().delete()
    return redirect('cart')


def checkout(request):
    order = Order.objects.filter(user=request.user, is_ordered=False).first()
    if not order:
        return redirect('cart')

    # Perform necessary operations for checkout, such as payment processing, address validation, etc.

    # Update the order status to indicate it has been placed
    order.is_ordered = True
    order.save()

    # Redirect to a success page or order summary page
    # return redirect('order_summary')
    print("Item ordered")
    return redirect('cart')