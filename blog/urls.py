from django.urls import path
from .models import User, Post
from . import views

urlpatterns = [
    # path('', views.homepage),
    path('', views.index),
    path('<slug:post_slug>', views.homepage, name='homepage')
]