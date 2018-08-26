from django.test import TestCase
from .models import Event


class TestViews(TestCase):

    def test_get_events_page(self):
        page = self.client.get("/events/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "events/events.html")
