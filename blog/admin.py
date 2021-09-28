from django.contrib import admin
from .models import User, Post


class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nickname',)}


admin.site.register(User, ClientAdmin)
admin.site.register(Post)

