from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from .views import single_product_view, product_list_view, DeleteTodoAPIView, UpdateTodoAPIView, CreateTodoAPIView, \
    ListTodoAPIView

urlpatterns = [
    path('products/<int:id>', single_product_view, name='single-product'),
    path('products/', product_list_view, name='products'),
    path("api/category/", ListTodoAPIView.as_view(), name="category_list"),
    path("api/category/create/", CreateTodoAPIView.as_view(), name="category_create"),
    path("api/category/update/<int:pk>/", UpdateTodoAPIView.as_view(), name="update_category"),
    path("api/category/delete/<int:pk>/", DeleteTodoAPIView.as_view(), name="delete_category"),
]
