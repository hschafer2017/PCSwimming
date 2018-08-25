from django.test import TestCase
from .models import AlumPost
from .forms import AlumPostForm
from accounts.models import Alumni, Swimmer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestAlumPostViews(TestCase):
    """Tests that you have to be registed as an Alumni to view Alumni page"""
    def test_get_alumposts_page(self):
        User.objects.create_user(
            username='Alumniuser1',
            email='Alumniuser1@example.com',
            password='password1')
        alumni = Alumni.objects.create(user_id='1', graduated='2009')
        self.client.login(username='Alumniuser1', password='password1')
        page = self.client.get("/alumni/")
        self.assertEqual(page.status_code, 200)
    
    def test_get_alumposts_page_as_swimmer(self):
        """Tests that Swimmers are blocked from the Alumni page"""
        User.objects.create_user(
            username='Swimuser1',
            email='Swimuser1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='Swimuser1', password='password1')
        page = self.client.get("/alumni/")
        self.assertEqual(page.status_code, 403)
    
    def test_get_new_alumpost_page(self):
        User.objects.create_user(
            username='Alumniuser1',
            email='Alumniuser1@example.com',
            password='password1')
        alumni = Alumni.objects.create(user_id='1', graduated='2009')
        self.client.login(username='Alumniuser1', password='password1')
        page = self.client.get("/alumni/new/")
        self.assertEqual(page.status_code, 200)
    
    def test_create_new_alumpost_form(self):
        User.objects.create_user(
            username='Alumniuser1', 
            email='Alumniuser1@example.com',
            password='password1')
        alumni = Alumni.objects.create(user_id='1', graduated='2009')
        self.client.login(username='Alumniuser1', password='password1')

        alum_post = AlumPost.objects.create(title='Test Alumni Post',
                                            content='Test Alumni Post Content')
        response = self.client.get("/alumni/")

        self.assertEqual(response.status_code, 200)

    def test_view_alumpost_detail(self):
        User.objects.create_user(
            username='Alumniuser1',
            email='Alumniuser1@example.com',
            password='password1')
        alumni = Alumni.objects.create(user_id='1', graduated='2009')
        self.client.login(username='Alumniuser1', password='password1')
        alum_post = AlumPost.objects.create(title='Test Alumni Post',
                                            content='Test Alumni Post Content')
        response = self.client.get("/alumni/1/".format(alum_post.pk))
        self.assertEqual(response.status_code, 200)

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("alumni/1")
        self.assertEqual(page.status_code, 404)
    
    def test_get_delete_post(self): 
        User.objects.create_user(
            username='Alumniuser1',
            email='Alumniuser1@example.com',
            password='password1')
        alumni = Alumni.objects.create(user_id='1', graduated='2009')
        self.client.login(username='Alumniuser1', password='password1')
        
        alum_post = AlumPost.objects.create(title='Test Alumni Post', content='Test Alumni Post Content')
        
        
        self.assertEqual(AlumPost.objects.count(), 1)
        response = self.client.get("/alumni/1".format(alum_post.pk))
        
        alum_post.delete()
        self.assertEqual(AlumPost.objects.count(), 0)
