from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from profiles.models import Swimmer

"""
Only swimmers have access to the posts/discussion page. If the user is not
    a swimmer or a superuser, return HttpResponseForbidden. If a user is not
    logged in, it redirects them to the login page. The posts app allows
    swimmers to create, read, update, and delete posts and comments for posts.
"""


def get_posts(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or
                    request.user.swimmer.graduation_year is not None):
                blogs = Post.objects.all()
                comments = Comment.objects.all()

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'posts/posts.html', {'blogs': blogs, 'comments':
                  comments})


def new_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or
                    request.user.swimmer.graduation_year is not None):
                if request.method == "POST":
                    form = PostForm(request.POST, request.FILES)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.owner = request.user
                        post.save()
                        return redirect('get_posts')
                else:
                    form = PostForm()

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'posts/postform.html', {'form': form})


def new_comment(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or
                    request.user.swimmer.graduation_year is not None):
                comments = Comment.objects.all()
                post = get_object_or_404(Post, pk=pk)
                blogs = Post.objects.all()
                if request.method == "POST":
                    form = CommentForm(request.POST)
                    if form.is_valid():
                        comment = form.save(commit=False)
                        comment.owner = request.user
                        comment.post = post
                        comment.save()
                        return redirect('post_detail', pk=post.pk)
                else:
                    form = CommentForm()

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'posts/commentform.html', {'form': form, 'blogs':
                  blogs, 'comments': comments, 'post': post})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.user.is_authenticated and request.user == post.owner or
            request.user.is_superuser):
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


def edit_comment(request, pk):
    comments = Comment.objects.all()
    blogs = Post.objects.all()
    comment = get_object_or_404(Comment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.owner or
            request.user.is_superuser):
        if request.method == "POST":
            form = CommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save()
                return redirect('post_detail', comment.post.id)
        else:
            form = CommentForm(instance=comment)
    else:
        return HttpResponseForbidden()

    return render(request, 'posts/commentform.html', {'form': form, 'blogs':
                  blogs, 'comments': comments, 'post': comment.post})


def delete_post(request):
    id = request.POST['blogs_id']
    post = get_object_or_404(Post, id=id)
    if (request.user.is_authenticated and request.user == post.owner or
            request.user.is_superuser):
        if request.method == 'POST':
            blogs = get_object_or_404(Post, pk=id)
            try:
                blogs.delete()
                messages.success(request,
                                 'You have successfully deleted the post!')

            except Post.DoesNotExist:
                messages.warning(request, 'The post could not be deleted.')
    else:
        return HttpResponseForbidden()

    return redirect('get_posts')


def delete_comment(request):
    id = request.POST['comment_id']
    pk = request.POST['blogs_id']
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, id=id)
    if (request.user.is_authenticated and request.user == comment.owner or
            request.user.is_superuser):
        if request.method == 'POST':
            try:
                comment.delete()
                messages.success(request,
                                 'You have successfully deleted the comment!')

            except Comment.DoesNotExist:
                messages.warning(request,
                                 'The comment could not be deleted.')
    else:
        return HttpResponseForbidden()
    return redirect('get_posts')


def post_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or request.user.is_authenticated and
                    request.user.swimmer.graduation_year is not None):
                blogs = Post.objects.all()
                comments = Comment.objects.all()
                post = get_object_or_404(Post, pk=pk)
                post.views += 1
                post.save()

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, "posts/postdetail.html", {'blogs': blogs,
                  'comments': comments, 'post': post})
