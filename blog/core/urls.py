from django.urls import path
from .views import home, post, category, author, dates

urlpatterns = [
    path("", home, name="home"),
    path("post/", post, name="post"),
    path("category/", category, name="category"),
    path("author/", author, name="author"),
    path("dates/", dates, name="dates"),
]