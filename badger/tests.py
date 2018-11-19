from django.urls import resolve
from django.test import TestCase
from django.views.generic import TemplateView


class HomePageTest(TestCase):

    def test_root_url_resolves_to_template_view(self):
        found = resolve('/badger/')
        self.assertEqual(found.func.__name__, "TemplateView")
