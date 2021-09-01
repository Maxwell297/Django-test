from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('posts/', HomePageView.as_view(), name='posts'),
]