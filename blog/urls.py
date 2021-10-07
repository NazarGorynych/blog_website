from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('<slug:user_slug>', views.homepage, name='homepage')
]