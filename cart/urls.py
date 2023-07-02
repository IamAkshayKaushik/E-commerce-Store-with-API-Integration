from django.urls import path
from cart.views import cart, add_to_cart, remove_from_cart, clear_cart, checkout


urlpatterns = [
    # Other URL patterns
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:order_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('clear/', clear_cart, name='clear_cart'),
    path('checkout/', checkout, name='checkout'),
]
