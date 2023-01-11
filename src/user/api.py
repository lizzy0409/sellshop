from django.urls import path
from .controller import login, register

urlpatterns = [
    path('login/', login, name='apilogin'),
    path('register/', register, name='apiregister'),
]