from django.shortcuts import render
from django.views import generic
from .models import Post, Page, Publication

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

class PublicationsList(generic.ListView):
    queryset = Publication.objects.filter(status=1).order_by('publish_date')
    template_name = 'blog/publications.html'

class PageView(generic.DetailView):
    model = Page
    template_name = 'blog/page.html'
