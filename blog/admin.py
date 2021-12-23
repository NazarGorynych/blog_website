from django.contrib import admin
from .models import User, Post, UserFollowing
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', ]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(UserFollowing)
