from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.template.defaultfilters import slugify


def index(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User = form.save()
            print('Success')
    form = UserForm
    return render(request, 'blog/register.html', {
        'form': form
    })

def homepage(request, user_slug):
    selected_user = User.objects.get(slug=user_slug)
    return render(request, 'blog/homepage.html', {
        'user_slug': selected_user
    })


