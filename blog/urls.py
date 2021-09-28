from django.urls import path
from .models import User, Post
from . import views

urlpatterns = [
    # path('', views.homepage),
    path('', views.index),
    path('<slug:user_slug>', views.homepage, name='homepage')
]