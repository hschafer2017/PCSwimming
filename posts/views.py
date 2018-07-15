from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, AlumPost
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.comments.view.moderate import perform_delete



# Create your views here - POSTS.
def get_posts(request): 
    if request.user.is_authenticated:
        blogs = Post.objects.all()
        comments = Comment.objects.all()
    else: 
        comments = Comment.objects.all()
        blogs = Post.objects.all()
    return render(request, 'posts/posts.html', {'blogs': blogs, 'comments': comments})

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

@login_required(login_url='/accounts/login/')
def edit_comment(request, pk): 
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_authenticated and request.user == comment.owner or request.user.is_superuser: 
        if request.method == "POST":
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save()
                return redirect('post_detail', comment.post.pk)        
        else:
            form = CommentForm(instance=comment)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'posts/commentform.html', {'form': form})



@login_required(login_url='/accounts/login/')
def delete_post(request):
   
    id = request.POST['blogs_id']
    if request.method == 'POST':
        blogs = get_object_or_404(Post, pk=id)
        try:
            blogs.delete()
            messages.success(request, 'You have successfully deleted the post')
        
        except:
            messages.warning(request, 'The post could not be deleted.')

    return redirect('get_posts')
    
    
    
@login_required(login_url='/accounts/login/')
def delete_comment(request):
    id = request.POST['comment_id']
    pk = request.POST['blogs_id']
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=id, pk=pk)
        try:
            comment.delete()
            messages.success(request, 'You have successfully deleted the comment')
        
        except:
            messages.warning(request, 'The comment could not be deleted.')

    return redirect('get_posts')
    
def post_detail(request, pk):
    blogs = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter()
    blogs.views += 1
    blogs.save()
    return render(request, "posts/postdetail.html", {'blogs': blogs, 'comments':comments})
    
def get_alum_posts(request): 
    alum_posts = AlumPost.objects.all()
    return render(request, "posts/alumniposts.html", {"alum_posts":alum_posts})