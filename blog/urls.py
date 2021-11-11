from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logged-out'),
    path('profile/', views.user_profile, name='profile'),
    path('<slug:user_slug>', views.homepage, name='homepage')
]