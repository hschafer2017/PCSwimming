from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404


class TestLoginView(TestCase):

    def test_get_login_form(self):
        response = self.client.get("/accounts/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_can_log_in(self):
        user1 = User.objects.create_user(
            username='testUser',
            email='testUser@example.com',
            password='passw0rd')

        response = self.client.get('/events/')
        self.assertEqual(response.context['user'], AnonymousUser())

        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'pass0word'
        })

        response = self.client.get('/accounts/login')

    def test_user_does_not_exist(self):
        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'pass0word'
        })
        self.assertFormError(response, 'form', None,
                             'Incorrect Username or Password!')


class TestRegisterUserTypesView(TestCase):
    def test_get_register_swimmer_form(self):
        response = self.client.get("/accounts/register_swimmer")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register_swimmer.html")

    def test_get_alumni_form(self):
        response = self.client.get("/accounts/register_alumni")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register_alumni.html")

    def test_can_register_swimmer(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post("/accounts/register_swimmer", {
            'username': 'testSwimmerUser22',
            'email': 'testSwimmerUser22@example.com',
            'password1': 'pa55w0rd!',
            'password2': 'pa55w0rd!',
            'graduation_year': '2020'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        self.assertEqual(User.objects.count(), 1)

    def test_can_register_alumni(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post("/accounts/register_alumni", {
            'username': 'testAlumniUser22',
            'email': 'testAlumniUser22@example.com',
            'password1': 'pa55w0rd!!',
            'password2': 'pa55w0rd!!',
            'graduated': '2002'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/events/')
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_form_does_not_register(self):
        response = self.client.post("/accounts/register", {
            'username': 'testUser2',
            'email': 'testUser2@example.com',
            'password1': 'pa55word',
            'password2': 'pa55word1!!',
        })
        self.assertEqual(User.objects.count(), 0)


class TestLogoutView(TestCase):
    def test_logout_form(self):
        response = self.client.get("/accounts/logout")
        self.assertRedirects(response, '/')
