from django.contrib import admin
from .models import Product, Rating, Color, Category, Size, Brand, ProductReview, ProductImageDetail

from modeltranslation.admin import TranslationAdmin


# Register your models here.


class ColorAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]
    list_filter = ['name', ]


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]
    list_filter = ['name', ]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class SizeAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]
    list_filter = ['name', ]


class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', ]
    list_filter = ['name', ]


class RatingAdmin(admin.ModelAdmin):
    search_fields = ['rating', ]
    list_display = ['rating', ]
    list_filter = ['rating', ]


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'price', 'image', 'desc', 'last_price', 'rating', ]
    list_display = ['title', 'price', ]
    list_filter = ['title', 'price', 'image', 'desc', 'last_price', 'rating', ]


class ProductReviewAdmin(admin.ModelAdmin):
    search_fields = ["full_name", "review", "email", "rating"]
    list_display = ["full_name", "review", "rating"]
    list_filter = ["full_name", "review", "email", "rating"]


class ProductImageDetailAdmin(admin.ModelAdmin):
    search_fields = ["product", "back_image", "side_image"]
    list_display = ["product", "back_image", "side_image"]
    list_filter = ["product", "back_image", "side_image"]


admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductImageDetail, ProductImageDetailAdmin)
