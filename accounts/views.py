from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from .forms import UserLoginForm, UserRegistrationForm, AlumniRegistrationForm, SwimmerRegistrationForm

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
                return redirect("get_events")
            else:
                login_form.add_error(None, "Incorrect Username or Password!")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})


def register_swimmer(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        swimmer_form = SwimmerRegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid() and swimmer_form.is_valid():
            user = registration_form.save()
            swimmer = swimmer_form.save(commit=False)
            swimmer.user = user
            swimmer.save()

            u = registration_form.cleaned_data['username']
            p = registration_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)

            if user is not None:
                login(request, user)
                return redirect("get_events")
            else:
                registration_form.add_error(None, "Swimmer registration unsuccessful, please try again.")
    else:
        registration_form = UserRegistrationForm()
        swimmer_form = SwimmerRegistrationForm()

    return render(request, 'accounts/register_swimmer.html',
                  {'form': registration_form, 'user_type_form': swimmer_form})


def register_alumni(request):
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        alumni_form = AlumniRegistrationForm(request.POST, request.FILES)

        if registration_form.is_valid() and alumni_form.is_valid():
            user = registration_form.save()
            alumni = alumni_form.save(commit=False)
            alumni.user = user
            alumni.save()

            u = registration_form.cleaned_data['username']
            p = registration_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)

            if user is not None:
                login(request, user)
                return redirect("get_events")
            else:
                user_form.add_error(None, "Alumni registration unsuccessful, please try again.")
    else:
        registration_form = UserRegistrationForm()
        alumni_form = AlumniRegistrationForm()

    return render(request, "accounts/register_alumni.html",
                  {'form': registration_form, 'user_type_form': alumni_form})


def do_logout(request):
    logout(request)
    return redirect('/')
