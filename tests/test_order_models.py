from order.models import Card, Payment_method, Order, Wish_list


def test_card_object_is_instance_of_model(db, card_obj):
    assert isinstance(card_obj, Card)


def test_payment_object_is_instance_of_model(db, payment_obj):
    assert isinstance(payment_obj, Payment_method)


def test_order_object_is_instance_of_model(db, order_obj):
    assert isinstance(order_obj, Order)


def test_wish_object_is_instance_of_model(db, wish_obj):
    assert isinstance(wish_obj, Wish_list)