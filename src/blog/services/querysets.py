from django.db.models import QuerySet
from blog.models import Blog, Comment_blog


def list_3_post() -> QuerySet:
    return Blog.objects.all().order_by('-id')[:3]


def post_comments(blog_id) -> QuerySet:
    return Comment_blog.objects.filter(blog_id=blog_id)
