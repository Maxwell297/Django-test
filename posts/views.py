from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'postshome.html'
    context_object_name = 'all_posts_list'