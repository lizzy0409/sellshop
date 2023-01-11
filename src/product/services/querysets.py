from django.db.models import QuerySet
from django.db.models import Q
from product.models import Product, Rating


#Daxil edilmiş məhsulun (product) review-larını qaytaran qs
# def review(id):
#     return Rating.objects.filter(id=id)
#
# def last_8_product():
#     return Product.objects.all().order_by('-id')[:8]

# def categories(category_id):
#     return Category.objects.get(id=category_id)
#
# def cat_product(category_id):
#     return Product.objects.filter(category_id=category_id)