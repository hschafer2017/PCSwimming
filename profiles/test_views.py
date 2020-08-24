from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404


class TestRegisterUserTypesView(TestCase):
    def test_get_register_swimmer_form(self):
        response = self.client.get("/register/register_swimmer/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/register_swimmer.html")

    def test_get_alumni_form(self):
        response = self.client.get("/register/register_alumni/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/register_alumni.html")

    def test_can_register_swimmer(self):
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post("/register/register_swimmer/", {
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

        response = self.client.post("/register/register_alumni/", {
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
        response = self.client.post("/profiles/register/", {
            'username': 'testUser2',
            'email': 'testUser2@example.com',
            'password1': 'pa55word',
            'password2': 'pa55word1!!',
        })
        self.assertEqual(User.objects.count(), 0)
