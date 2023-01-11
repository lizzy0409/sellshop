import pytest

from product.models import Category, Color, Brand, Size, Rating, ProductReview, Product
from order.models import Card, Payment_method, Order, Wish_list
from user.models import Profile
from core.models import Creative_team, Contact
from blog.models import Blog, Like_blog, Comment_blog


@pytest.fixture
def creative_team_obj():
    return Creative_team.objects.create(
        name='Aytac',
        image='hey.jpg',
        facebook='aytac',
        twitter='aytac',
        google='aytac',
        website='aytac',
        mdi_dribbble='aytac'
    )


@pytest.fixture
def contact_obj():
    return Contact.objects.create(
        name='Aytac',
        email='aytac@gmail.com',
        message='hey hey'
    )


@pytest.fixture
def user_obj():
    return Profile.objects.create(
        first_name='Dunya',
        last_name='Okean',
        username='earth',
        email='earth@gmail.com',
        phone='0554563254',
        address='Solar system',
        country='Sun',
        additional='im home for earthlings'
    )


@pytest.fixture
def color_obj():
    return Color.objects.create(
        name='Red'
    )


@pytest.fixture
def category_obj():
    return Category.objects.create(
        name='Cap'
    )


@pytest.fixture
def size_obj():
    return Size.objects.create(
        name='XL'
    )


@pytest.fixture
def brand_obj():
    return Brand.objects.create(
        name='LC Waikiki'
    )



@pytest.fixture
def product_obj(color_obj, category_obj, size_obj, brand_obj):
    return Product.objects.create(
        title='Sviter',
        price=100,
        image='hey.jpg',
        color=color_obj,
        category=category_obj,
        size=size_obj,
        desc='Comfyy',
        brand=brand_obj,
        last_price=200,
        status='NEW'
    )


@pytest.fixture
def rating_obj(product_obj):
    return Rating.objects.create(
        product_id=product_obj,
        rating=4
    )


@pytest.fixture
def product_review_obj(product_obj):
    return ProductReview.objects.create(
        full_name='Aytac',
        product_id=product_obj,
        email='aytacaliyeva133@gmail.com',
        review='Nice and cool',
        rating=4,
    )


@pytest.fixture
def card_obj(user_obj, product_obj):
    return Card.objects.create(
        user_id=user_obj,
        product_id=product_obj
    )


@pytest.fixture
def payment_obj():
    return Payment_method.objects.create(
        name='Card'
    )


@pytest.fixture
def order_obj(payment_obj, card_obj):
    return Order.objects.create(
        order_no=1,
        payment_id=payment_obj,
        card_id=card_obj
    )


@pytest.fixture
def wish_obj(user_obj, product_obj):
    return Wish_list.objects.create(
        user_id=user_obj,
        product_id=product_obj
    )


@pytest.fixture
def blog_obj(user_obj):
    return Blog.objects.create(
        title='10 Fall clothes',
        image='fall.jpg',
        desc='cool styles',
        author=user_obj,
        no_of_likes=1,
        no_of_comments=2
    )


@pytest.fixture
def like_blog_obj(user_obj, blog_obj):
    return Like_blog.objects.create(
        blog_id=blog_obj,
        user_id=user_obj
    )


@pytest.fixture
def comment_blog_obj(user_obj, blog_obj):
    return Comment_blog.objects.create(
        blog_id=blog_obj,
        user_id=user_obj,
        comment='Nice',
        email='aytac@gmail.com'
    )



















