from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            User = form.save()
            print('Success')
    form = CustomUserCreationForm
    return render(request, 'blog/register.html', {
        'form': form
    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_profile(request):
    return render(request, 'blog/user-profile.html')


def user_logout(request):
    logout(request)
    return redirect(index)

def homepage(request, user_slug):
    selected_user = User.objects.get(slug=user_slug)
    return render(request, 'blog/homepage.html', {
        'user_slug': selected_user
    })


