from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseForbidden

# Create your views here - POSTS.
def get_posts(request): 
    if request.user.is_authenticated:
        blogs = Post.objects.all()
    else: 
        blogs = Post.objects.all()
    return render(request, 'posts/posts.html', {'blogs': blogs})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        
    return render(request, 'posts/postform.html', {'form': form})


def post_detail(request, pk):
    blogs = get_object_or_404(Post, pk=pk)
    blogs.views += 1
    blogs.save()
    return render(request, "posts/postdetail.html", {'blogs': blogs})