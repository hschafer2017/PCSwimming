from django.forms import ModelForm, TextInput
from .models import AlumPost
from django import forms


class AlumPostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'TITLE'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'CONTENT'}))
    
    class Meta:
        model = AlumPost
        fields = ['title', 'content', 'published_date', 'image']