from django.test import TestCase
from .models import Event, Document

class TestCheckoutModels(TestCase):

    def test_create_event(self):
        event = Event(name='meet', location='home', day='2018-10-05', start_time='18:00')
        event.save()
        self.assertFalse(event.notes)
        self.assertEqual(event.name, 'meet')
        self.assertEqual(event.location, 'home')
        self.assertEqual(event.day, '2018-10-05')
        self.assertEqual(event.start_time, '18:00')
        
    def test_upload_document(self):
        document = Document(file='schedule.pdf')
        self.assertFalse(document.name)
        self.assertEqual(document.file, 'schedule.pdf')