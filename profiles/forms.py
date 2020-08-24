from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Alumni, Swimmer


class UserLoginForm(forms.Form):
    """
    Used by the user to enter login credentials
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'USERNAME'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'PASSWORD'}))


class UserRegistrationForm(UserCreationForm):
    """
    Used by the user to sign up with the website
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'USERNAME'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'EMAIL'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'PASSWORD'}))
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput(attrs={'placeholder': 'CONFIRM PASSWORD'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class SwimmerRegistrationForm(forms.ModelForm):
    graduation_year = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'GRADUATION YEAR'}))

    class Meta:
        model = Swimmer
        fields = ['graduation_year']


class AlumniRegistrationForm(forms.ModelForm):
    graduated = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'GRADUATION YEAR'}))

    class Meta:
        model = Alumni
        fields = ['graduated']
