from django.apps import apps
from django.test import TestCase
from .apps import HomeConfig


class TestHomeConfig(TestCase):

    def test_home_app(self):
        self.assertEqual("home", HomeConfig.name)
        self.assertEqual("home", apps.get_app_config("home").name)
