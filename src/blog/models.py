from django.db import models
from datetime import datetime
from user.models import Profile

from product.models import Category


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', max_length=100)
    desc = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=18, on_delete=models.CASCADE)
    no_of_likes = models.IntegerField()
    no_of_comments = models.IntegerField()
    published_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class Like_blog(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Comment_blog(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    email = models.CharField(max_length=50)
