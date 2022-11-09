from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('posts.urls', namespace='posts')),
    path('about/', include('about.urls', namespace='about')),
    path('profile/<username>/', include('posts.urls', namespace='posts')),
    path('posts/<posts_id>/', include('posts.urls', namespace='posts')),
    path('posts/', include('posts.urls', namespace='create')),
    path('posts/', include('posts.urls', namespace='edit')),
]
