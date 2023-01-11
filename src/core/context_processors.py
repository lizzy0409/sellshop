import json

from core.forms import ContactForm
from product.models import Category

from order.models import Order

from order.utils import guestOrder


def get_in_touch(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context = {
        "contact_form": form
    }
    return context


def categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return context

