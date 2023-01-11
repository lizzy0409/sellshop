from django.db.models import Min, Max, Avg
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Brand, Category, Color, Size, ProductReview, Rating
from .forms import ProductReviewForm
from django.contrib.auth.decorators import login_required

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import CategorySerializer

from django.core.paginator import Paginator

from order.models import Order


@login_required(login_url='login')
def single_product_view(request, id):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    product = get_object_or_404(Product, id=id)
    rating = request.POST.get('rating')
    print(rating)

    commments = Paginator(ProductReview.objects.filter(product_id=product), 4)
    page = request.GET.get('page')
    all_commments = commments.get_page(page)

    if request.method == "POST":
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            Rating.objects.create(product_id=product, rating=rating)
            average_rating = Rating.objects.filter(product_id=id).aggregate(Avg('rating'))['rating__avg']
            Product.objects.filter(id=id).update(total_rating=average_rating)

            new_comment = form.save(commit=False)
            new_comment.product_id = product
            form.save()

            return redirect(f"/products/{id}")
    else:
        form = ProductReviewForm()

    context = {
        "product_form": form,
        "all_commments": all_commments,
        'product': product,
        'items': items,
        'order': order,
    }
    return render(request, 'single-product.html', context)


@login_required(login_url='login')
def product_list_view(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

    products = Product.objects.values().order_by('-id')[:4]

    p = Paginator(Product.objects.all(), 4)

    trend_products = Product.objects.filter(status='TREND')[:3]
    first = trend_products[0]
    second = trend_products[1]
    third = trend_products[2]
    brands = Brand.objects.values()
    categories = Category.objects.values()
    colors = Color.objects.filter()
    sizes = Size.objects.values()
    whole_product = Product.objects.values().count()

    CATID = request.GET.get('categories')
    COLORID = request.GET.get('color')
    SIZEID = request.GET.get('size')
    BRANDID = request.GET.get('brand')
    FilterPrice = request.GET.get('FilterPrice')
    if CATID:
        p = Paginator(Product.objects.filter(category=CATID), 4)
    if COLORID:
        p = Paginator(Product.objects.filter(color=COLORID), 4)
    if SIZEID:
        p = Paginator(Product.objects.filter(size=SIZEID), 4)
    if BRANDID:
        p = Paginator(Product.objects.filter(brand=BRANDID), 4)
    if FilterPrice:
        int_FilterPrice = int(FilterPrice)
        p = Paginator(Product.objects.filter(price__lte=int_FilterPrice), 4)

    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))

    page = request.GET.get('page')
    products_list = p.get_page(page)
    best_brand = Product.objects.filter(status='BEST BRAND')[0]

    filter_product = products.count()

    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'sizes': sizes,
        'colors': colors,
        'whole_product': whole_product,
        'filter_product': filter_product,
        'first': first,
        'second': second,
        'third': third,
        'products_list': products_list,
        'min_price': min_price,
        'max_price': max_price,
        'best_brand': best_brand,
        'items': items,
        'order': order,
        # 'products_list_count': products_list_count,
    }

    return render(request, 'product-list.html', context=context)


class ListTodoAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateTodoAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateTodoAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteTodoAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


