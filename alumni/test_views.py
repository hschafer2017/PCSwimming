from django.test import TestCase
from .models import AlumPost
from .forms import AlumPostForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestAlumPostViews(TestCase):
    def test_get_alumposts_page(self):
        User.objects.create_user(
            username='Alumniuser1', 
            email='Alumniuser1@example.com',
            password='password1')
        self.client.login(username='Alumniuser1', password='password1')
        page = self.client.get("/alumni/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "alumni/alumniposts.html")
    
    def test_get_new_alumpost_page(self):
        User.objects.create_user(
            username='Alumniuser1', 
            email='Alumniuser1@example.com',
            password='password1')
        self.client.login(username='Alumniuser1', password='password1')
        page = self.client.get("/alumni/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "alumni/alumnipostform.html")
    
    def test_create_new_alumpost_form(self):
        
        User.objects.create_user(
            username='Alumniuser1', 
            email='Alumniuser1@example.com',
            password='password1')
        self.client.login(username='Alumniuser1', password='password1')
        
        alum_post = AlumPost.objects.create(title='Test Alumni Post', content='Test Alumni Post Content')
        response = self.client.get("/alumni/")
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "alumni/alumniposts.html")
        
    def test_view_alumpost_detail(self):
        
        User.objects.create_user(
            username='Alumniuser1', 
            email='Alumniuser1@example.com',
            password='password1')
        self.client.login(username='Alumniuser1', password='password1')
        
        alum_post = AlumPost.objects.create(title='Test Alumni Post', content='Test Alumni Post Content')
        response = self.client.get("/alumni/1/".format(alum_post.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "alumni/alumnipostdetail.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("alumni/1")
        self.assertEqual(page.status_code, 404)
    
    def test_get_delete_post(self): 
        User.objects.create_user(
            username='Alumniuser1', 
            email='Alumniuser1@example.com',
            password='password1')
        self.client.login(username='Alumniuser1', password='password1')
        
        alum_post = AlumPost.objects.create(title='Test Alumni Post', content='Test Alumni Post Content')
        
        
        self.assertEqual(AlumPost.objects.count(), 1)
        response = self.client.get("/alumni/1".format(alum_post.pk))
        
        alum_post.delete()
        self.assertEqual(AlumPost.objects.count(), 0)