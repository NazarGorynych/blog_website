from django.shortcuts import render, redirect
from .models import User, Post
from .forms import CustomUserCreationForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/index.html'
    queryset = Post.objects.all()
    #
    # def get_queryset(self):
    #     return Post.objects.all()
    # #
    # def get_context_data(self, **kwargs):
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     return context

# class PostView(generic.DetailView):
#     model = Post
#     template_name = 'blog'


def index(request):
    # all_posts = Post.objects.all()
    return render(request, 'blog/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.user_save()
            print('Success')
        else:
            print('failure')
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
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect(index)


def user_profile(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if User.is_authenticated:
            if form.is_valid:
                form = form.save(commit=False)
                form.author = request.user
                form.save()
    form = PostForm()
    return render(request, 'blog/user-profile.html', {'form': form})



def homepage(request, user_slug):
    selected_user = User.objects.get(slug=user_slug)
    return render(request, 'blog/homepage.html', {
        'user_slug': selected_user
    })


