from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from multiselectfield import MultiSelectField

from user.models import Profile


class Color(models.Model):
    COLORS = (
        ('orange', '#FFA500'),
        ('black', '#000000'),
        ('blue', '#0000FF'),
        ('pink', '#FFC0CB'),
        ('grey', '#808080'),
        ('green', '#00FF00'),
        ('brown', '#964B00'),
        ('purple', '#800080'),
        ('red', '#EE4B2B'),
        ('white', '#FFFFFF'),
        ('yellow', '#FFFF00'),
    )

    name = models.CharField(max_length=50, choices=COLORS)

    def __str__(self):
        return self.name


class Category(models.Model):
    # CATEGORIES = (
    #     ('Tshirt', 'Tshirt'),
    #     ('Shorts', 'Shorts'),
    #     ('Hoodie', 'Hoodie'),
    #     ('Skirt', 'Skirt'),
    #     ('Cap', 'Cap'),
    #     ('Dress', 'Dress'),
    #     ('Jeans', 'Jeans'),
    #     ('Shoes', 'Shoes'),
    #     ('Coat', 'Coat'),
    #     ('Suit', 'Suit'),
    #     ('Hat', 'Hat'),
    #     ('Socks', 'Socks'),
    #     ('Gloves', 'Gloves'),
    #     ('Scarf', 'Scarf'),
    #     ('Tie', 'Tie'),
    #     ('Swimsuit', 'Swimsuit'),
    #     ('Gym clothes', 'Gym clothes'),
    # )
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Size(models.Model):
    SIZES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('3XL', '3XL'),
        ('4XL', '4XL'),
        ('5XL', '5XL'),
    )

    name = models.CharField(max_length=50, choices=SIZES)

    def __str__(self):
        return self.name


class Brand(models.Model):
    BRANDS = (
        ('LOUIS', 'LOUIS'),
        ('GUCCI', 'GUCCI'),
        ('HERMES', 'HERMES'),
        ('PRADA', 'PRADA'),
        ('CHANEL', 'CHANEL'),
        ('RALPH', 'RALPH'),
        ('BURBERRY', 'BURBERRY'),
        ('HOUSE', 'HOUSE'),
        ('FENDI', 'FENDI'),
        ('NIKE', 'NIKE'),
    )

    name = models.CharField(max_length=50, choices=BRANDS)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('NEW', 'NEW'),
        ('TREND', 'TREND'),
        ('OUT OF STOCK', 'OUT OF STOCK'),
        ('BEST BRAND', 'BEST BRAND'),
        ('SOON', 'SOON'),
    )

    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products', max_length=100)
    category = models.ManyToManyField(Category)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    desc = models.TextField()
    brand = models.ManyToManyField(Brand)
    last_price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    purchase_time = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default='WOMEN', choices=(('WOMEN', 'WOMEN'), ('MEN', 'MEN')))
    total_rating = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Rating(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()


class ProductReview(models.Model):
    full_name = models.CharField(max_length=50)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    review = models.CharField(max_length=20)
    rating = models.CharField(max_length=5, default=1,
                              choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")))
    published_date = models.DateTimeField(default=datetime.now)


class LikedProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class ProductImageDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    back_image = models.ImageField(upload_to='products', max_length=100)
    side_image = models.ImageField(upload_to='products', max_length=100)
