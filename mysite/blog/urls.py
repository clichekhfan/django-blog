from django.urls import path
from django.conf.urls import url, include
from blog.views import list_view, detail_view, stub_view

urlpatterns = [
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', list_view, name="blog_index"),
]
