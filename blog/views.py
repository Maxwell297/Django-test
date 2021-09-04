from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_post_detail.html'