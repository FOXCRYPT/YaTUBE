from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
  

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    
    return render(request, 'posts/group_list.html', context) 


#def group(request):
    #template = 'posts/'
    #text = 'Это главная страница проекта Yatube'
    #context = {
    #    'text': text,
    #}
    #return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования


# Create your views here.
