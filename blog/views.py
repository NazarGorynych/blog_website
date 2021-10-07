from django.shortcuts import render
from .models import User
from .forms import UserForm


def index(request):
    return render(request, 'blog/index.html')


def register(request):
    form = UserForm
    return render(request, 'blog/register.html', {
        'form': form
    })

def homepage(request, user_slug):
    selected_user = User.objects.get(slug=user_slug)
    return render(request, 'blog/homepage.html', {
        'user_slug': selected_user
    })


