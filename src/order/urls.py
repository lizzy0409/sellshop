from django.urls import path
from .views import *

urlpatterns = [
    path('order-complete/', order_complate, name='ordercomplete'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('wishlist/', wishlist_page, name='wishlist'),
    path('update_item/', update_item, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path("api/order_items/", ListOrderItemAPIView.as_view(), name="category_list"),
    path("api/order_items/delete/<int:pk>/", DeleteOrderItemAPIView.as_view(), name="delete_category"),
    path("order_items/", order_items, name="order_items"),
]
