from django.contrib import admin
from .models import Order, Wish_list, OrderItem, ShippingAddress

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'complete', 'date_ordered', 'transaction_id', ]
    list_display = ['customer', 'complete', 'date_ordered', 'transaction_id', ]
    list_filter = ['customer', 'complete', 'date_ordered', 'transaction_id', ]


class Wish_listAdmin(admin.ModelAdmin):
    search_fields = ['product_id', 'user_id', ]
    list_display = ['product_id', 'user_id', ]
    list_filter = ['product_id', 'user_id', ]


class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ['product', 'order', 'quantity', 'date_added', ]
    list_display = ['product', 'order', 'quantity', 'date_added', ]
    list_filter = ['product', 'order', 'quantity', 'date_added', ]


class ShippingAddressAdmin(admin.ModelAdmin):
    search_fields = ['customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added', ]
    list_display = ['customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added', ]
    list_filter = ['customer', 'order', 'address', 'city', 'state', 'zipcode', 'date_added', ]


admin.site.register(Order, OrderAdmin)
admin.site.register(Wish_list, Wish_listAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)