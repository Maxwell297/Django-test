from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('blog/post/<int:pk>/', BlogDetailView.as_view(), name='blog_post_detail'),
    path('blog/', BlogListView.as_view(), name='blog'),
]