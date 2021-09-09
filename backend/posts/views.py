from posts.models import Post
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostsListView(ListView):
   model = Post
   template_name = 'posts/index.html'

class PostsCreateView(CreateView):
   model = Post
   template_name = 'posts/post_new.html'
   fields = ['title', 'author', 'content']

class PostsDetailView(DetailView):
   model = Post
   template_name = 'posts/post_detail.html'

class PostsUpdateView(UpdateView):
   model = Post
   template_name = 'posts/post_edit.html'
   fields = ['title', 'content']

class PostsDeleteView(DeleteView):
   model = Post
   template_name = 'posts/post_delete.html'
   success_url = reverse_lazy('posts')
