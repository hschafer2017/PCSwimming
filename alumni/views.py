from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import AlumPost
from .forms import AlumPostForm
from accounts.models import Alumni
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def get_alum_posts(request):
    """If the user is not an Alumni, return HttpResponseForbidden"""
    try:
        if (request.user.is_superuser or
                request.user.alumni.graduated is not None):
                alum_posts = AlumPost.objects.all()

    except Alumni.DoesNotExist:
        return HttpResponseForbidden()

    return render(request, "alumni/alumniposts.html", 
                  {"alum_posts": alum_posts})


def new_alum_post(request):
    try:
        if (request.user.is_superuser or
            request.user.alumni.graduated is not None):
            if request.method == "POST":
                form = AlumPostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.owner = request.user
                    post.save()
                    return redirect('get_alum_posts')
            else:
                form = AlumPostForm()

    except Alumni.DoesNotExist:
        return HttpResponseForbidden()

    return render(request, 'alumni/alumnipostform.html', {'form': form})


def alum_post_detail(request, pk):
    try:
        if (request.user.is_superuser or
            request.user.alumni.graduated is not None):
            alum_posts = AlumPost.objects.all()
            post = get_object_or_404(AlumPost, pk=pk)

    except Alumni.DoesNotExist:
        return HttpResponseForbidden()

    return render(request, "alumni/alumnipostdetail.html",
                  {'alum_posts': alum_posts, 'post': post})


def delete_alum_post(request):
    pk = request.POST['blogs_id']
    if (request.user.is_authenticated and request.user == alumpost.owner or 
        request.user.is_superuser):
        if request.method == 'POST':
            blogs = get_object_or_404(AlumPost, pk=pk)
            try:
                blogs.delete()
                messages.success(request, 'You have successfully deleted the post!')

            except:
                messages.warning(request, 'The post could not be deleted.')
    else:
        return HttpResponseForbidden()
    return redirect('get_alum_posts')


def edit_alum_post(request, pk):
    post = get_object_or_404(AlumPost, pk=pk)
    if (request.user.is_authenticated and request.user == post.owner or 
        request.user.is_superuser):
        if request.method == "POST":
            form = AlumPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect('alum_post_detail', post.pk)
        else:
            form = AlumPostForm(instance=post)
    else:
        return HttpResponseForbidden()

    return render(request, 'alumni/alumnipostform.html', {'form': form})
