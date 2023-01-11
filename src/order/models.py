from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from product.models import Product
from user.models import Profile


class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderItems])
        return total

    @property
    def get_cart_items(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    COUNTRIES = (
        ('Azerbaijan', 'Azerbaijan'),
        ('Turkey', 'Turkey'),
        ('USA', 'USA'),
    )

    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=False, default='Azerbaijan', choices=COUNTRIES)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=False)
    address = models.TextField(max_length=500, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Wish_list(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
