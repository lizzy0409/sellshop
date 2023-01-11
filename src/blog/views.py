from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog
from django.db import connection
from django.contrib.auth.decorators import login_required

from order.models import Order


@login_required(login_url='login')
def single_blog(request, id):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    blog = Blog.objects.get(id=id)
    related_blogs = Blog.objects.filter(category=blog.category)

    return render(request, 'single-blog.html',
                  {'blog': blog, 'order': order, 'items': items, 'related_blogs': related_blogs})


@login_required(login_url='login')
def blog_view(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    blogs = Paginator(Blog.objects.all(), 3)

    page = request.GET.get('page')
    blogs = blogs.get_page(page)

    return render(request, 'blog.html', {'blogs': blogs, 'order': order, 'items': items})
