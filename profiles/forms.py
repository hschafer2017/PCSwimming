from django import forms
from django.core.exceptions import ValidationError

from .models import Swimmer

class SignupForm(forms.Form):
    graduation_year = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'GRADUATION YEAR'}))

    def signup(self, request, user):
        user.save()
        Swimmer.objects.filter(user=user).update(
            graduation_year=self.cleaned_data['graduation_year'])
