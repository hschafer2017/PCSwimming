from django.shortcuts import render
from .models import AlumPost

# Create your views here.

def get_alum_posts(request): 
    alum_posts = AlumPost.objects.all()
    return render(request, "alumni/alumniposts.html", {"alum_posts":alum_posts})