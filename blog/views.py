from django.shortcuts import render
from django.views import generic
from .models import Post, Page

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'

class PageView(generic.DetailView):
    model = Page
    template_name = 'page.html'