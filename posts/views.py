from django.shortcuts import render
from django.views import generic

from .models import Post

def index(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)
