from django.apps import apps
from django.test import TestCase
from .apps import AlumniConfig


class TestAlumniConfig(TestCase):

    def test_alumni_app(self):
        self.assertEqual("alumni", AlumniConfig.name)
        self.assertEqual("alumni", apps.get_app_config("alumni").name)
