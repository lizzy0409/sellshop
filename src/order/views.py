from django.core import serializers
from django.forms import models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from .models import Order, OrderItem, ShippingAddress
from product.models import Product
import datetime

from .serializers import OrderItemSerializer
from .utils import guestOrder


@login_required(login_url='login')
def order_complate(request):
    return render(request, 'order-complete.html')


@login_required(login_url='login')
def cart_view(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'cart.html', context=context)


@login_required(login_url='login')
def checkout_view(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    context = {
        'items': items,
        'order': order,

    }
    return render(request, 'checkout.html', context=context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId: ', productId)
    print('Action: ', action)

    customer = request.user
    product = Product.objects.get(id=productId)
    print(customer, product)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    print(action)

    if action == 'delete':
        orderItem.delete()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    print('Data: ', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        phone_number=data['form']['number'],
        country=data['shipping']['country'],
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],

    )

    return JsonResponse('Payment complete', safe=False)


@login_required(login_url='login')
def wishlist_page(request):
    return render(request, 'wishlist.html')


def order_items(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    serialized_data = serializers.serialize("json", items)
    serialized_data = json.loads(serialized_data)

    context = {
        'items': serialized_data,
        'order': models.model_to_dict(order),
    }

    return JsonResponse(context)


class ListOrderItemAPIView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CreateOrderItemAPIView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class UpdateOrderItemAPIView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class DeleteOrderItemAPIView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
