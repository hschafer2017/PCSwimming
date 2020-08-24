from django.test import TestCase
from .models import Swimmer, Alumni


class TestUserTypesModel(TestCase):

    def test_register_as_swimmer(self):
        swimmer = Swimmer(user_id='1')
        swimmer.save()
        self.assertEqual(swimmer.user_id, "1")
        self.assertFalse(swimmer.graduation_year)

    def test_register_as_alumni(self):
        alumni = Alumni(user_id='1')
        alumni.save()
        self.assertEqual(alumni.user_id, "1")
        self.assertFalse(alumni.graduated)
