from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Post
from .forms import PostForm

def index(request):
    posts_list = Post.objects.order_by('-votes')
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)

def post_new(request):
    if request.method == 'POST':
        if request.is_ajax():
            form = PostForm(request.POST)
            post_text = request.POST.get('post_text')
            data = {"post_text": post_text}
            if form.is_valid():
                post = form.save(commit=False)
                post.pub_date = timezone.now()
                post.save()
            return JsonResponse(data)
    else:
        form = PostForm()
    return render(request,'posts/post_edit.html', {'form': form})

def vote(request, post_id):
    if request.method == 'POST':
        if request.is_ajax():
            up_down = request.POST.get('up_down')
            post = get_object_or_404(Post, pk=post_id)

            if up_down == "plus":
                post.votes += 1
                post.save()
            else:
                post.votes -= 1
                post.save()

            data = {"votes": post.votes}
            return JsonResponse(data)

    return HttpResponseRedirect(reverse('posts:index'))

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/post.html', context)
