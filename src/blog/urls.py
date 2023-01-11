from django.urls import path
from .views import *

urlpatterns = [
    path('blog/<id>', single_blog, name='singleblog'),
    path('blogs', blog_view, name='blogs'),
]
