from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Swimmer, Alumni

class TestViews(TestCase):

    def test_get_home_page_logged_in_swimmer(self):
        User.objects.create_user(
            username='user1', 
            email='user1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='user1', password='password1')
        page = self.client.get("/events/")
        self.assertEqual(page.status_code, 200)
    
    def test_get_home_page_logged_in_alumni(self):
        User.objects.create_user(
                username='user1', 
                email='user1@example.com',
                password='password1')
        alumni = Alumni.objects.create(user_id='1', graduated='2009')
        self.client.login(username='user1', password='password1')
        page = self.client.get("/events/")
        self.assertEqual(page.status_code, 200)
    
    def test_not_logged_in_redirect(self):
        page = self.client.get("")
        self.assertEqual(page.status_code, 200)