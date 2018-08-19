from django.apps import apps
from django.test import TestCase
from .apps import EventsConfig


class TestEventsConfig(TestCase):

    def test_events_app(self):
        self.assertEqual("events", EventsConfig.name)
        self.assertEqual("events", apps.get_app_config("events").name)