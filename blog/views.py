from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def homepage(request):
    return render(request, 'blog/homepage.html')