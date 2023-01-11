from product.models import Color, Category, Size, Brand, Product, Rating, ProductReview


def test_color_object_is_instance_of_model(db, color_obj):
    assert isinstance(color_obj, Color)


def test_category_object_is_instance_of_model(db, category_obj):
    assert isinstance(category_obj, Category)


def test_size_object_is_instance_of_model(db, size_obj):
    assert isinstance(size_obj, Size)


def test_brand_object_is_instance_of_model(db, brand_obj):
    assert isinstance(brand_obj, Brand)


def test_product_object_is_instance_of_model(db, product_obj):
    assert isinstance(product_obj, Product)


def test_rating_object_is_instance_of_model(db, rating_obj):
    assert isinstance(rating_obj, Rating)


def test_product_review_object_is_instance_of_model(db, product_review_obj):
    assert isinstance(product_review_obj, ProductReview)





















