from blog.models import Blog, Like_blog, Comment_blog


def test_blog_object_is_instance_of_model(db, blog_obj):
    assert isinstance(blog_obj, Blog)


def test_like_blog_object_is_instance_of_model(db, like_blog_obj):
    assert isinstance(like_blog_obj, Like_blog)


def test_comment_blog_object_is_instance_of_model(db, comment_blog_obj):
    assert isinstance(comment_blog_obj, Comment_blog)