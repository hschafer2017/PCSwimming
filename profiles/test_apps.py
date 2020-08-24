from django.apps import apps
from django.test import TestCase
from .apps import profilesConfig


class TestprofilesConfig(TestCase):

    def test_profiles_app(self):
        self.assertEqual("profiles", profilesConfig.name)
        self.assertEqual("profiles", apps.get_app_config("profiles").name)
