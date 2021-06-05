from django.urls import path
from django.conf.urls import url, include
from blog.views import BlogListView, BlogDetailView, stub_view

urlpatterns = [
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", BlogListView.as_view(), name="blog_index"),
]
