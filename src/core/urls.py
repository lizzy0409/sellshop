from django.urls import path
from .views import home_page, AboutPage, contact_page, search_products, error
from .context_processors import get_in_touch

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact/', contact_page, name='contact'),
    path("get/", get_in_touch, name="get-in-touch"),
    path("search_products/", search_products, name="search_products"),
    path("error/", error, name="error"),
    # path("load-more-data/", load_more_data, name="load_more_data"),
]
