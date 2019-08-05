from django.shortcuts import render,redirect,get_object_or_404
import pdb
from bab_app.models import Post

def home(request):
    latest_posts = Post.objects.order_by('created_at')[:5]
    all_posts = Post.objects.all()
    return render(request, 'index.html', {'latest_posts':latest_posts, 'all_posts': all_posts}) 