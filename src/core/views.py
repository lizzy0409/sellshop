from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from product.models import Product, Category, ProductImageDetail

from order.models import Order
from .models import Creative_team, Contact_details


@login_required(login_url='login')
def search_products(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    if request.method == 'POST':
        searched = request.POST.get('searched')
        products = Product.objects.filter(title__contains=searched)
        return render(request, 'search_products.html', {'searched': searched, 'products': products, 'order': order, 'items': items})
    else:
        return render(request, 'search_products.html', {})


@login_required(login_url='login')
def home_page(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    soon = ProductImageDetail.objects.all()[0]
    new_products = Product.objects.filter(status='NEW')[:8]
    popular_products = Product.objects.filter(total_rating__gte=4)[:8]
    total_data = Product.objects.count()

    best_seller_product_purchase_time = Product.objects.aggregate(Max("purchase_time"))['purchase_time__max']
    best_seller_products = Product.objects.filter(purchase_time__gte=best_seller_product_purchase_time-10)

    categories = Category.objects.all()
    trend_products = Product.objects.filter(status='TREND')[:3]
    first = trend_products[0]
    second = trend_products[1]
    third = trend_products[2]
    featured_products1 = Product.objects.filter(purchase_time__gte=2)[:4]

    context = {
        'first': first,
        'second': second,
        'third': third,
        'featured_products1': featured_products1,
        'categories': categories, 'soon': soon,
        'new_products': new_products,
        'popular_products': popular_products,
        'best_seller_products': best_seller_products,
        'order': order,
        'items': items,
        'total_data': total_data,

    }
    return render(request, 'index.html',
                  context=context)


# def load_more_data(request):
#     offset = int(request.GET['offset'])
#     limit = int(request.GET['limit'])
#     total_data = Product.objects.count()
#
#     featured_products1 = Product.objects.filter(purchase_time__gte=2)[offset: offset+limit]
#
#     t = render_to_string('product-list.html', {'data': featured_products1})
#     return JsonResponse({'data': t})


class AboutPage(View):
    def get(self, request):
        teams = Creative_team.objects.all()
        return render(request, 'about.html', context={'teams': teams})


# @login_required(login_url='login')
# def about_page(request):
#     teams = Creative_team.objects.all()
#     return render(request, 'about.html', context={'teams': teams})


@login_required(login_url='login')
def contact_page(request):
    contact_detail = Contact_details.objects.all()[0]
    return render(request, 'contact.html', context={'contact_detail': contact_detail})


def error(request):
    return render(request, 'error.html')
