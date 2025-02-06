from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    # Fetch all published posts
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    # Fetch a single post using its slug
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})