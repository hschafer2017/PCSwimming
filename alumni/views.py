from django.shortcuts import render, get_object_or_404, redirect
from .models import AlumPost

# Create your views here.

def get_alum_posts(request): 
    alum_posts = AlumPost.objects.all()
    return render(request, "alumni/alumniposts.html", {"alum_posts":alum_posts})
    
def new_alum_post(request):
    if request.method == "POST":
        form = AlumPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('get_alum_posts')
    else:
        form = PostForm()
        
    return render(request, 'alumni/alumnipostform.html', {'form': form})
    
def alum_post_detail(request, pk): 
    alum_posts = AlumPost.objects.all()
    post = get_object_or_404(AlumPost, pk=pk)
    return render(request, "alumni/alumnipostdetail.html", {'alum_posts': alum_posts, 'post': post})
    