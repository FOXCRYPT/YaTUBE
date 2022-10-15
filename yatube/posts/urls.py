from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.index, name='home'),
    #path('MANAGER/', include('posts.urls', namespace='MAIN')),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    #path('', views.group, name='group'),
    
] 
