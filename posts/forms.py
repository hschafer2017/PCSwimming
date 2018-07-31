from django.forms import ModelForm, TextInput
from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'TITLE'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'CONTENT'}))
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date']
    
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'CONTENT'}))
    class Meta:
        model = Comment
        fields = ['content']