from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here - POSTS.
def get_posts(request): 
    if request.user.is_authenticated:
        blogs = Post.objects.all()
        comments = Comment.objects.all()
    else: 
        comments = Comment.objects.all()
        blogs = Post.objects.all()
    return render(request, 'posts/posts.html', {'blogs': blogs, 'comments':comments})

@login_required(login_url='/accounts/login/')
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
 
@login_required(login_url='/accounts/login/')    
def new_comment(request, pk): 
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        
    return render(request, 'posts/commentform.html', {'form': form})


@login_required(login_url='/accounts/login/')
def edit_post(request, pk): 
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated and request.user == post.owner or request.user.is_superuser: 
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect('post_detail', post.pk)        
        else:
            form = PostForm(instance=post)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'posts/postform.html', {'form': form})


def post_detail(request, pk):
    blogs = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter()
    blogs.views += 1
    blogs.save()
    return render(request, "posts/postdetail.html", {'blogs': blogs, 'comments':comments})