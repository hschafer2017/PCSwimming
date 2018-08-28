from django.test import TestCase
from .models import AlumPost


class TestUserTypesModel(TestCase):

    def test_create_alumni_post(self):
        alum_post = AlumPost(title='Alumni Test', content='Some test content.')
        alum_post.save()
        self.assertEqual(alum_post.title, "Alumni Test")
        self.assertEqual(alum_post.content, "Some test content.")
        self.assertFalse(alum_post.image)
