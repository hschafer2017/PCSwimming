from django.test import TestCase
from .forms import ItemRequirementsForm
from .models import ItemRequirements


class TestItemRequirementsForms(TestCase):              
    def test_item_requirements(self):
        form = ItemRequirementsForm({'notes':'Small'})
        self.assertTrue(form.is_valid())
