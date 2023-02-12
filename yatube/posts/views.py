from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Group, Post, User
from .utils import scroll_posts


def index(request):
    post_list = Post.objects.select_related('author', 'group')
    page_obj = scroll_posts(request, post_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')
    page_obj = scroll_posts(request, posts)
    context = {
        'page_obj': page_obj,
        'group': group,
    }

    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.select_related('group')
    page_obj = scroll_posts(request, posts)
    context = {
        'page_obj': page_obj,
        'author': author,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,

    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', username=request.user)
    form = PostForm()
    return render(request, 'posts/create_post.html',
                  {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if not post.author == request.user:
        form = PostForm(instance=post)
        return render(request, 'posts/create_post.html',
                   {'form': form})
    if not request.method == 'POST':
        form = PostForm(instance=post)
        return render(request, 'posts/create_post.html',
                   {'form': form})
    if form.is_valid():
        form.save(commit=True)
        return redirect('posts:post_detail', post.id)
