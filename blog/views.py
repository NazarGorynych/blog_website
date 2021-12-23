from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Post, UserFollowing
from .forms import CustomUserCreationForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/index.html'
    queryset = Post.objects.all()

# class PostView(generic.DetailView):
#     model = Post
#     template_name = 'blog'


class UserSearchView(generic.ListView):
    model = User
    template_name = 'blog/subscriptions.html'
    context_object_name = 'users'

    def get_queryset(self):
        # result = super(UserSearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = User.objects.filter(username__icontains=query)
            users = []
            for object in result:
                users.append(object)
        else:
            users = None
        return users


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
            user = authenticate(username=cd['username'],
                                password=cd['password'])
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
    return redirect(user_login)


def user_profile(request, id):
    selected_user = get_object_or_404(User, pk=id)
    master_user = request.user
    followed = False
    if UserFollowing.objects.filter(master_user=master_user, following_user=selected_user):
        followed = True
    if selected_user == master_user:             # display form for Posting for currently signed in user
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid:
                form = form.save(commit=False)
                form.author = request.user
                form.save()
    form = PostForm()
    print(followed)
    return render(request, 'blog/user-profile.html', {
        'form': form,
        'selected_user': selected_user,
        'master_user': master_user,
        'followed': followed
        })


def follow_user(request, id):
    master_user = request.user
    selected_user = get_object_or_404(User, pk=id)
    isfollowed = UserFollowing.objects.filter(master_user=master_user,
                                                     following_user=selected_user)
    if isfollowed:
        isfollowed.delete()                                         # unfollow the followed user
    else:
        UserFollowing.objects.create(master_user=master_user,       # follow the selected user
                                     following_user=selected_user
                                     )
    return redirect(user_profile, id)


def homepage(request, user_slug):
    selected_user = User.objects.get(slug=user_slug)
    return render(request, 'blog/homepage.html', {
        'user_slug': selected_user
    })


