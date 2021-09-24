from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def homepage(request, post_slug):
    selected_post = Post.objects.get(slug=post_slug)
    return render(request, 'blog/homepage.html', {
        'post_slug':selected_post
    })