from django.test import TestCase
from .forms import AlumPostForm
from .models import AlumPost

# Create your tests here.



class TestAlumPostForms(TestCase):              
    def test_alum_post_content(self):
        form = AlumPostForm({'Title':'Title'})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])
        
    def test_alum_post_image_required(self):
        form = AlumPostForm({'Title':'Title', 'Content':'some content'})
        self.assertFalse(form.is_valid())
        print(form.errors['image'], ['This field is required.'])