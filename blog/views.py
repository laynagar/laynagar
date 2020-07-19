from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 9
    template_name = 'blog/blog.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
