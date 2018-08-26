from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def get_index(request):
    if request.user.is_authenticated:
        return redirect('get_events')
    return render(request, 'home/index.html')
