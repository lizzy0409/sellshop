from django.contrib import admin
from .models import Blog, Like_blog, Comment_blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'image', 'desc', 'author', 'no_of_likes', 'no_of_comments', 'published_date', ]
    list_display = ['title', 'author', 'published_date']
    list_filter = ['title', 'image', 'desc', 'author', 'no_of_likes', 'no_of_comments', 'published_date', ]

class Like_blogAdmin(admin.ModelAdmin):
    search_fields = ['blog_id', 'user_id' ]
    list_display = ['blog_id', 'user_id' ]
    list_filter = ['blog_id', 'user_id' ]

class Comment_blogAdmin(admin.ModelAdmin):
    search_fields = ['blog_id', 'user_id', 'comment', 'date', 'email', ]
    list_display = ['blog_id', 'user_id', 'comment', 'date', 'email' ]
    list_filter = ['blog_id', 'user_id', 'comment', 'date', 'email' ]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Like_blog, Like_blogAdmin)
admin.site.register(Comment_blog, Comment_blogAdmin)