from django.views import generic
from django.shortcuts import render
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(ststus=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
