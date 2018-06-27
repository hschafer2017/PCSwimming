from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from .forms import UserLoginForm, UserRegistrationForm
# Create your views here - ACCOUNTS.

def do_login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)
    
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})
    
def register(request):
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            
            u = registration_form.cleaned_data['username']
            p = registration_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                registration_form.add_error(None, "Can't log in now, try later.")
    else:
        registration_form = UserRegistrationForm()
    
    
    return render(request, 'accounts/register.html', {'form': registration_form})
    
def profile(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return render(request, 'accounts/profile.html', {'form':form}, {'posts', posts})
    else:
        form = PhotoForm()
    return render(request, 'accounts/profile.html', {'form':form}, {'posts': posts})
    
def do_logout(request): 
    logout(request)
    return redirect('/')