from django.shortcuts import render
from .models import User
# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def homepage(request, user_slug):
    selected_user = User.objects.get(slug=user_slug)
    return render(request, 'blog/homepage.html', {
        'user_slug':selected_user
    })