"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    PostsListView, PostsCreateView, PostsDetailView, 
    PostsUpdateView, PostsDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostsDetailView.as_view(), name='post_detail'),
    path('posts/new', PostsCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostsUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostsDeleteView.as_view(), name='post_delete'),
]
