from django.urls import resolve
from django.test import TestCase
from django.views.generic import TemplateView
from django.http import HttpRequest
from .models import Employee


class BadgerHomePageTest(TestCase):

    def test_root_url_resolves_to_template_view(self):
        found = resolve('/badger/')
        self.assertEqual(found.func.__name__, "TemplateView")

    def test_badger_home_page_returns_correct_html(self):
        response = self.client.get('/badger/')

        #
        # Decode the response and strip the newlines so startswith and
        # endwith matched will work.
        #
        html = response.content.decode('utf8').strip('\n')

        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('Badger', html)
        self.assertTrue(html.endswith('</html>'))


class EmployeeCreateViewTests(TestCase):

    def test_create_employee(self):
        self.client.post('/badger/employee_create/',
                {'first_name':"fred", 'last_name': "bloggs",  })
        self.assertEqual(Employee.objects.last().first_name, "fred")
