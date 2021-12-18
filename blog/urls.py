from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('subscriptions/', views.UserSearchView.as_view(), name='subscriptions'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logged-out'),
    path('profile/<int:id>/', views.user_profile, name='profile'),
    # path('search_results/', views.search_for_user, name='search_for_user'),
    path('<slug:user_slug>', views.homepage, name='homepage')
]